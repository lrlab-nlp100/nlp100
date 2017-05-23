#! /usr/bin/env python

# create name:area database as db0 on local redis.

import redis
import json

import sys


def main():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    keys = r.keys()
    vs = r.mget(keys)
    print(len(list(filter(lambda v: v == b"Japan", vs))))


if __name__ == "__main__":
    main()
