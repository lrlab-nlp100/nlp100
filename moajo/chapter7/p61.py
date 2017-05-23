#! /usr/bin/env python

# create name:area database as db0 on local redis.

import redis
import json

import sys


def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("unexpected argument length")
    arg = sys.argv[1]
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    print(r.get(arg))


if __name__ == "__main__":
    main()
