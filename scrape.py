"""
A script designed to collect *user_id* information from StackExchange's sites.

Copyright (c) 2016, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""

import argparse
import requests
from bs4 import BeautifulSoup
from collections import namedtuple

BS4_PARSER = 'html.parser'
URL_PREFIX = 'http://'
URL_KERNEL = '.stackexchange.com'
URL_SUFFIX = '/users?tab=NewUsers&sort=creationdate'
BLACKLIST = ['ja.', 'meta']
FILENAME = 'sites.txt'


class CustomFormatter(argparse.RawDescriptionHelpFormatter):
    """Inheriting from the *argparse* module, this custom formatter
       is designed to build a more aesthetic command-line interface."""

    def __init__(self, prog):
        super().__init__(prog, max_help_position=28)

    def _format_action_invocation(self, action):
        command = '{} ({})'.format(*action.option_strings)
        if action.metavar:
            command = '{} {}    '.format(command, action.metavar)
        return command


def set_command_list():
    """Provide a list of command-line options."""

    argdict = {
        'formatter_class': CustomFormatter,
        'description': ("A script designed to collect *user_id* "
                        "information from StackExchange's sites."),
        'epilog': """
  Copyright (c) 2016, Nebil Kawas García
  This source code is subject to the terms of the Mozilla Public License.
  You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>."""}

    parser = argparse.ArgumentParser(**argdict)
    parser.add_argument('-l', '--list', action='store_true',
                        help="list (almost) all StackExchange's sites")
    parser.add_argument('-s', '--site', type=str, metavar=('SITENAME'),
                        help="show last *user_id* for a specific site",
                        dest='curl')
    return parser.parse_args()


def scrape(curl):
    """
    Collect data from StackExchange's sites.

    parameters:  @curl: a StackExchange's site CURL <str>
    ===========
                 If @curl is None, it will get all sites.
    """

    def get_last_user_id(curl):
        """
        Fetch the most recent *user_id*.

        parameters:  @curl: a StackExchange's site CURL <str>
        ===========

           returns:  the newest *user_id* of the given CURL.
           ========

           example:  {@curl = 'chess'}
           ========  should return... an integer (e.g. 9876)
        """

        if '.' not in curl:
            curl += URL_KERNEL

        rget = requests.get(URL_PREFIX + curl + URL_SUFFIX)
        soup = BeautifulSoup(rget.content, BS4_PARSER)

        # search for the most recent user.
        user = soup.find('div', class_='user-details').find('a')['href']
        user_id = user.split('/')[2]
        return int(user_id)

    def process(line):
        """
        Parse information from a single line.

        parameters:  @line: a single line of text <str>
        ===========

           returns:  a named three-item tuple with: name,
           ========                                 CURL,
                                                    newest *user_id*.

           example:  {@line = 'Unix & Linux                     | unix'}
           ========  should return... namedtuple('Unix & Linux', 'unix', <int>)
        """

        site = namedtuple('site', ['name', 'curl', 'last_user_id'])
        name, curl = line.split('|')
        curl = curl.strip()

        return site(name, curl, get_last_user_id(curl))

    if curl is None:  # ergo, no command-line arguments were given.
        with open(FILENAME, 'r') as sites:
            all_sites = [process(site) for site in sites]
            all_sites.sort(key=lambda site: site.last_user_id, reverse=True)
        for site in all_sites:
            print('{} | {:20} | {:9,}'.format(*site))
    else:
        last_user_id = get_last_user_id(curl)
        print('{}: {:,}+ users'.format(curl, last_user_id))


def print_all_sites():
    """Fetch a list of all StackExchange's sites."""

    def get_curl(url):
        """
        Clean a site URL by removing its affixes.

        parameters:  @url: a StackExchange's site URL <str>
        ===========

           returns:  the CURL (core URL) of the given site.
           ========

           example:  {@url = 'http://ux.stackexchange.com'}
           ========  should return... 'ux'.
        """

        curl = url.replace(URL_PREFIX, '') \
                  .replace(URL_KERNEL, '')
        return curl

    rget = requests.get('http://stackexchange.com/sites?view=list#users')
    soup = BeautifulSoup(rget.content, BS4_PARSER)
    all_sites = soup('div', class_='lv-info')
    for site in all_sites:
        anchor = site.find('h2').find('a')
        name = anchor.string
        curl = get_curl(anchor['href'])

        # filter some sites.
        if any(item in curl for item in BLACKLIST):
            continue
        print('{:36} | {}'.format(name, curl))

if __name__ == '__main__':
    clargs = set_command_list()
    if clargs.list:
        print_all_sites()
    else:
        scrape(clargs.curl)
