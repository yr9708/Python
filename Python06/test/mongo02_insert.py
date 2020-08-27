# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint
client = MongoClient('localhost',27017)
db = client.test
score = db.score

# { name:자기이름, kor:?, eng:?, math:?} 등록하자

result01 = score.insert_one({
        'name' : '이제훈',
        'kor' : 100,
        'eng' : 80,
        'math' : 40
    })
print(result01.inserted_id)

result02 = score.insert_many([
    {
        'name' : '한지용',
        'kor' : 100,
        'eng' : 100,
        'maht' :100
    },
    {
        'name' : '강여림',
        'kor' : 90,
        'eng' : 90,
        'maht' :90
    },
        {
        'name' : '김지후',
        'kor' : 80,
        'eng' : 80,
        'maht' :80
    },
    {
        'name' : '위영석',
        'kor' : 70,
        'eng' : 70,
        'maht' :70
    },
])

print(result02.inserted_ids)