# -*- coding:utf-8 -*-
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.test
score = db.score

# name이 자기이름은 document 하나를 찾아서, 삭제하자

result01 = score.delete_one(
        {'name':'강여림'}
    )

print(result01.deleted_count)

result02 = score.delete_many({'math':{'$lt':100}})
print(result02.deleted_count)
print('-------------------')

print(score.delete_many({}).deleted_count) # 조건을 안줬기 때문에 나머지 다 삭제해라