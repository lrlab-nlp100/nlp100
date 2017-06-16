# -*- coding: utf-8 -*-
import plyvel
cnt = 0
my_db = plyvel.DB('/Users/haraita/Documents/Program/nlp.ldb')
for name,area in my_db:
    if area == b'Japan':
        cnt += 1
print(cnt)
my_db.close()
