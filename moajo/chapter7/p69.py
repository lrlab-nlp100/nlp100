#! /usr/bin/env python

# create name:area database as db0 on local redis.

import redis
import json

import sys, json
from chapter7.p60 import read_json
from chapter7.class_artist import Artist
from pymongo import MongoClient
from http import server
from urllib.parse import urlparse,unquote
import html


def start(port, callback):
    def handler(*args):
        return CallbackServer(callback, *args)

    sv = server.HTTPServer(('', int(port)), handler)
    sv.serve_forever()


class CallbackServer(server.SimpleHTTPRequestHandler):
    def __init__(self, callback, *args):
        self.callback = callback
        server.SimpleHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        parsed_path = urlparse(self.path)
        print(parsed_path.geturl())
        if parsed_path.geturl() == "/p69_index.js":
            with open("./p69_index.js", "r", encoding="utf-8") as f:
                js = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(js.encode())
            return
        with open("./p69_index.html", "r", encoding="utf-8") as f:
            html = f.read()
        query = parsed_path.query
        print(query)
        self.send_response(200)
        self.end_headers()
        result = self.callback(query)
        print(result)
        a = html.replace("<!--replace by python(see p69.py)-->", result).encode()
        print(a)
        # message = '\r\n'.join(result)
        self.wfile.write(a)
        return


def main():
    client = MongoClient("localhost:27017")
    c = client["p64"]["artists"]

    def callback(query):
        print("query: {0}".format(query))
        spl = query.split("&")
        print(len(spl))
        q = {}
        for qq in filter(lambda l:l!="",spl):
            split = qq.split("=")
            q[split[0]] = unquote(split[1])
        find_obj={}
        if "name" in q:
            find_obj["name"]=q["name"]
        if "alias" in q:
            find_obj["aliases.name"] = {"$in": [q["alias"]]}
        if "tag" in q:
            find_obj["tags.value"] = {"$in": [q["tag"]]}

        buf = ""
        for data in c.find(find_obj).limit(50):
            del data["_id"]
            s = json.dumps(data)
            s = "<li>{0}</li>".format(html.escape(s))
            buf += s
        return buf

    start(8000, callback)
    # sv = server.HTTPServer(("",8000),server.SimpleHTTPRequestHandler)
    # sv.serve_forever()
    return

    # json_ = read_json()
    # artists = list(map(lambda j: Artist(j), json_))
    # for a in artists:
    #     print(a.json)
    #     c.insert_one(a.json)


    # c.insert_one({"aaa":3333})
    # c.remove({"aaa":3333})
    # raging.count
    # for data in result.limit(10):
    #     print(data)
        # print(result.count())


if __name__ == "__main__":
    main()
