#!/usr/bin/python3
from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        data = response.read()
        utf_data = data.decode('utf-8')
        res_type = type(data)
        print("Body response:")
        print("\t- type: {}".format(res_type))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(utf_data))
