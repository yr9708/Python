# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=mon')
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)
webtoons = soup.find('ul',{'class' :'img_list'}).find_all('li')
lst = list()
for webtoon in webtoons :
    title = webtoon.find('dl').find('dt').find('a')['title']
    star = webtoon.find_all('dd')[1].find('div').find('strong').text
   #print('{} [{}]'.format(title,star))
    tmp = {}
    tmp['title'] = title
    tmp['star'] = star
    # {'title' : '제목', 'star' : 0.00} 가지고 왔어 가지고 온걸 list에 반복적으로 append 했어
    lst.append(tmp)
# [{'title' : '제목' , 'star' : 0.00}, {'title' : '제목' , 'star' : 0.00 }]
# 얘는 json 형태가 아니야, 이건 key : value 형태가 아니고 배열형태야
# array가 value 형태로 들어갈 수 있기 때문에
# 얘를 다시 한번 key로 감싸주겠다.

# print(lst)
res = {}
res['webtoons'] = lst
# {'webtoons' : [{'title' : '제목' , 'star' : 0.00}, {'title' : '제목' , 'star' : 0.00 }] ...}  이렇게 json 형태로 바꿔준것
# print(res)

res_json = json.dumps(res, ensure_ascii=False) # dumps는 바꾸는 것
print(res_json)

with open('webtoons.json','w',encoding='utf-8') as f:
    f.write(res_json)

# 강사님 코드
# webtoons = soup.find('ul',class_='img_list')
# dl = webtoons.select('dl')
# 
# for chd in dl :
#     title = chd.find('a').text
#     star = chd.find('strong').text
#     print('{} [{}]'.format(title,star))