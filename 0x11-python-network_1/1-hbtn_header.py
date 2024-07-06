#!/usr/bin/python3
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as e:
        print(e.info()["X-Request-Id"])
