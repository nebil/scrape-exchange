"""
A script designed to collect *user_id* information from StackExchange's sites.

Copyright (c) 2016, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""

import requests
from bs4 import BeautifulSoup

URL_PREFIX = 'http://'
URL_SUFFIX = '/users?tab=NewUsers&sort=creationdate'
BLACKLIST = ['ja.', 'meta']
FILENAME = 'sites.txt'


def scrape():
    def get_last_user_id(curl):
        if '.com' not in curl:
            curl += '.stackexchange.com'

        rget = requests.get(URL_PREFIX + curl + URL_SUFFIX)
        soup = BeautifulSoup(rget.content, 'html.parser')

        # search for the most recent user.
        user = soup.find('div', class_='user-details').find('a')['href']
        user_id = user.split('/')[2]
        return int(user_id)

    def process(line):
        name, curl = line.split('|')
        curl = curl.strip()

        return [name, curl, get_last_user_id(curl)]

    with open(FILENAME, 'r') as sites:
        all_sites = [process(site) for site in sites]
        all_sites.sort(key=lambda site: site[2], reverse=True)
    for site in all_sites:
        print('{} | {:18} | {:9,}'.format(*site))


def print_all_sites():
    def get_curl(url):
        curl = url.replace(URL_PREFIX, '') \
                  .replace('.stackexchange.com', '')
        return curl

    rget = requests.get('http://stackexchange.com/sites?view=list#users')
    soup = BeautifulSoup(rget.content, 'html.parser')
    all_sites = soup('div', class_='lv-info')
    for site in all_sites:
        anchor = site.find('h2').find('a')
        name = anchor.string
        curl = get_curl(anchor['href'])

        # filter some sites.
        if any(item in curl for item in BLACKLIST):
            continue
        print('{:36} | {}'.format(name, curl))

scrape()
print("--------")
print_all_sites()
