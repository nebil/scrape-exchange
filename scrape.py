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
FILENAME = 'sites.txt'


def scrape():
    def get_last_user_id(curl):
        rget = requests.get(URL_PREFIX + curl + URL_SUFFIX)
        soup = BeautifulSoup(rget.content, 'html.parser')

        # search for the most recent user.
        user = soup.find('div', class_='user-details').find('a')['href']
        user_id = user.split('/')[2]
        return user_id

    with open(FILENAME, 'r') as sites:
        for site in sites:
            name, curl = site.split('|')
            curl = curl.strip()
            if '.com' not in curl:
                curl += '.stackexchange.com'

            print(name, get_last_user_id(curl))

scrape()
