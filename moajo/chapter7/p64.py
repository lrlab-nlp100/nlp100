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
    # for data in c.find():
    #     print(data)

if __name__ == "__main__":
    main()
