# -*- coding:utf-8 -*-
# 튜토리얼 보면서 따라하기 
# https://pymongo.readthedocs.io/en/stable/tutorial.html
from pymongo import MongoClient

# MongoDB와 연결
# client = MongoClient('127.0.0.1',27017) # 나중에 학원db open되면 iptime.qclass.org 가능
client = MongoClient('mongodb://localhost:27017')

# 연결된 client에서 db와 연결
# db = client.test
db = client['test']

# 연결된 db에서 collection 가져오기
# collection = db.score
collection = db['score']

for doc in collection.find(): 
    print(doc)