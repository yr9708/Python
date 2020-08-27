# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)
db = client.test
score = db.score

aggr = score.aggregate([
        {"$match":{'kor':{'$gte':90}}},
        {'$group':{'_id':'mysum', 'sum':{'$sum':'$kor'}}}
    ])

print(aggr)
pprint.pprint(list(aggr))