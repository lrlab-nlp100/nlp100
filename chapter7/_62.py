import redis

def getArtistInArea(area):
	r = redis.Redis(host='localhost', port=6379, db=0)
	keys = r.keys('*')
	cnt = 0
	for key in keys:
		if r.get(key).decode('utf-8') == area:
			cnt += 
print(cnt)


if __name__ == '__main__':
	getArtistInArea('Japan')

