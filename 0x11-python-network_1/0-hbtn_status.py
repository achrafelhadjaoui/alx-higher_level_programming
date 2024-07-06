#!/usr/bin/python3
from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    # Create a Request object
    req = request.Request(url)
    
    # Open the URL using the Request object
    with request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

