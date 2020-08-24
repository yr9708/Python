# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request #파이선 내부에 자동으로 있는 라이브러리

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
# print(resp)
soup = BeautifulSoup(resp, 'html.parser')
#print(soup)
movies = soup.find_all('dl', class_='lst_dsc') # dl 태그를 가지고 올건데 class가 lst_dsc 인걸로 가지고 올거야
# print(movies)
# print(movies[0])

# 제목과 별점만 출력하자.
for movie in movies :
    title = movie.find('a').text
    star = movie.find('span',class_='num').text
    print('{},[{}]'.format(title,star))

# print(soup.find('dt',class_='tit').find('a'))
# print(soup.find('div',class_='star_t1').find('span',class_='num'))