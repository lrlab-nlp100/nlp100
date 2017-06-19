# -*- coding: utf-8 -*-
import plyvel
my_db = plyvel.DB('/Users/haraita/Documents/Program/nlp.ldb')
print(my_db.get('Oasis'.encode('utf-8')))
my_db.close()
