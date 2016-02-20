"""
A script designed to collect *user_id* information from StackExchange's sites.

Copyright (c) 2016, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""

import requests
from bs4 import BeautifulSoup

URL = 'http://stackoverflow.com/users?tab=NewUsers&sort=creationdate'


def get_last_user_id():
    rget = requests.get(URL)
    soup = BeautifulSoup(rget.content, 'html.parser')

    # search for the most recent user.
    user = soup.find('div', class_='user-details').find('a')['href']
    user_id = user.split('/')[2]
    print(user_id)

get_last_user_id()
