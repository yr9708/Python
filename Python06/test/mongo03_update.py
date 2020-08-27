# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)
db = client['test']
score = db['score']

# name이 자기이름인 document를 찾아서 국어점수를 0점으로 만들자

result01 = score.update_one(
        {'name':'강여림'},
        {'$set':{'kor':0}}
    )

print(result01.matched_count)
print(result01.modified_count)

print('------------------')

result02 = score.update_many({'eng':{'$lte':90}}, {'$set':{'eng':0}})
print(result02.matched_count)
print(result02.modified_count)

