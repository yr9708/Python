# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

tag = input('search keyword : ')
url = 'https://www.instagram.com/explore/tags/' + tag
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)

res = soup.find('div',{'class':'KL4Bh'})
print(res) # 브라우저에서 화면이 다 랜더링 된 이후에 크롤링 하기 위해서 selenium을 사용한다.