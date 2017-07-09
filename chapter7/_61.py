import redis

def getArtistArea(name):
	r = redis.Redis(host='localhost', port=6379, db=0)
	area = r.get(name)
	print(area)


if __name__ == '__main__':
	getArtistArea('Oasis')