# -*- coding:utf-8 -*-

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def root():
    return render_template("index.html")
    

@app.route('/crawling')
def crawling():
    resp = requests.get('https://movie.naver.com/movie/running/current.nhn#')
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # naver 영화에서, 제목과 별점을 크롤링하여 json으로 리턴하자.
    # { movies : [{"title" : '다만 악에서 구하소서', "star" : '7.79'}, {...}, {...}, ...]}
    
    # dl태그 중에서 class이름이 lst_dsc인 애들을 movies에 담았다.
    movieall = soup.find_all('dl', class_='lst_dsc')
    
    # 얘는 배열이라 [] 로 나와
    movies = list()

    for movie in movieall:
        title = movie.find('a').text
        star = movie.find('span', class_='num').text
    
        # 딕셔너리 {}로 나와
        tmp = {} # tmp = dict()와 같은 의미.
        tmp['title'] = title
        tmp['star'] = star
        movies.append(tmp)
    
    res = {}
    res['movies'] = movies

    res_json = json.dumps(res, ensure_ascii=False)
    print(res_json)

    return res_json
    
    
    
    
if __name__ == '__main__':
    app.run(port='8585')