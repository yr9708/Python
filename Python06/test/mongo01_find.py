# -*- coding:utf-8 -*-


from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

# cursor 객체
cursor = score.find()
print(cursor)

for doc in cursor :
    pprint.pprint(doc)

print('-----------------')

lee = score.find({'name':'이순신'})
print(lee) # cursor라는 객체 덩어리의 값을 print (find 로 찾을때는 무조건 cursor객체로 찾아와준다)
for doc in lee:
    # print(doc)
    pprint.pprint(doc)
    
hong = score.find_one({'name':'홍길동'})
pprint.pprint(hong)    

print('------------------')

# 국어점수가 60점보다 더 큰 document들을 모두 출력하자
res = score.find({
        'kor' : {'$gte':60}
    })
for doc in res :
    pprint.pprint(doc)
    
    
print('------------------')
print('score collection 안에 있는 document의 총 갯수 : ',score.count_documents({}))