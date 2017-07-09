import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
#r.flushall()

with open("artist.json", "r") as f:
	content = []
	for line in f:
		j = json.loads(line)
		key = j['name']
		value = j.get('tags')
		r.set(key,value)