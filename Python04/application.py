# -*- coding:utf-8 -*-

from flask import Flask, render_template, request

# jinja2 가지고 우리가 template을 사용을 하고 있는데, html이 있고 html 위에 템플릿을 살짝 걸친다 라고 생각하는게 좋을 것 같아요.
# server side rendering SSR - > 서버에서 화면을 만들거에요, java, 디장고
# client side rendering CSR -> 프론트에서 화면을 만들거에요, 그래서 서버에서는 데이터만 준다.
# Sinlge Page Application SPA는 CSR의 한종류, 서버에서 넘겨준 데이터를 받아서 화면이 깜빡이지않고 하나의 화면에서 모든것을 처리 (ajax)

app = Flask(__name__)

@app.route('/')
def root(): 
    return '''
    <a href="/hello">hello</a><br/>
    <input type="button" value="hello" onclick='location.href="/hello/name"'/>
'''

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None): # 초기값 None (넘어오는게 없으면), 무언가 값이 넘어오면 name에 치환이 된다.
    return render_template("hello.html",name=name) # hello.html 파일을 템플렛을 이용해서 그려줄건데 name=name의 값을 이용해서 넘겨줄거야 


@app.route('/test',methods=['POST'])
def test():
    return render_template("test.html",test=request.form['command']) # 요청들어오는 것중에 form 태그 안에 command이름으로 되어있는 애를 받아서 다시 test.html 에다가 test라는 이름으로 보낼거야

if __name__ == '__main__':
    app.run(host='localhost',port='8585')
