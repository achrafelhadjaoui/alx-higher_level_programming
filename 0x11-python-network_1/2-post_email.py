#!/usr/bin/python3
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    data = {}
    url = sys.argv[1]
    data['email'] = sys.argv[2]
    url_values = parse.urlencode(data).encode('utf-8')
    full_url = url + '?' + url_values

    with request.urlopen(full_url) as res:
        print("Your email is: {}".format(res.read().decode('utf-8')))
