#! /usr/bin/env python

# create name:area database as db0 on local redis.

import redis
import json

import sys, json
from chapter7.p60 import read_json
from chapter7.class_artist import Artist
from pymongo import MongoClient


def main():
    # json_ = read_json()
    # artists = list(map(lambda j: Artist(j), json_))
    client = MongoClient("localhost:27017")
    c = client["p64"]["artists"]
    # for a in artists:
    #     print(a.json)
    #     c.insert_one(a.json)


    # c.insert_one({"aaa":3333})
    # c.remove({"aaa":3333})
    search_alias = "Spoom"
    result = c.find({"aliases.name": {"$in": [search_alias]}})
    for data in result:
        print(data)
        # print(result.count())


if __name__ == "__main__":
    main()
