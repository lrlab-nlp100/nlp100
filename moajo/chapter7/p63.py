#! /usr/bin/env python

# create name:area database as db0 on local redis.

import redis
import json

import sys, json
from chapter7.p60 import read_json
from chapter7.class_artist import Artist


def main():
    json_ = read_json()
    artists = list(map(lambda j: Artist(j), json_))
    r = redis.Redis(host='127.0.0.1', port=6379, db=1)
    r.flushall()  # remove all
    for a in artists:
        if a.tags is not None:
            s = json.dumps(a.tags)
            r.set(a.name, s)
        else:
            r.set(a.name, None)


if __name__ == "__main__":
    main()
