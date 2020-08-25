# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__) # 현재 파이선 파일의 이름(프로젝트의 이름) 갖다가 flask로 application으로 만들어 주는것

@app.route('/') # java의 Annotation과 같다, localhost:5000/ 루트로 요청된 것.
def hello() :
    return 'Hello, World!' 

if __name__ == '__main__':
    app.run()