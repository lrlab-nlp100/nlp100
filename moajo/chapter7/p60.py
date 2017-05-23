#! /usr/bin/env python

# create name:area database as db0 on local redis.

import redis
import json
from chapter7.class_artist import Artist


def read_json():
    with open("./artist.json", "r", encoding="utf-8") as f:
        s = f.readlines()
    return json.loads("[" + ",".join(s) + "]")


def main():
    json_ = read_json()
    artists = list(map(lambda j: Artist(j), json_))
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    r.flushall()  # remove all
    for a in artists:
        print(a.name, a.area)
        r.set(a.name, a.area)


if __name__ == "__main__":
    main()
