#!/usr/bin/python3
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as e:
        data = e.read()
        utf_data = data.decode('utf-8')
        resType = type(data)
        print("Body response:$\n\t- type: {}\n\t- content: \
{}\n\t- utf8 content: {}".format(resType, data, utf_data))
