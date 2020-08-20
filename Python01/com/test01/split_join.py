# -*- coding:utf-8 -*-
import re 


# split 
str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ')
print(arr01)

arr02 = str01.split(' ', 2) # 공백2개로 자른것 maxsplit (몇개를 자를거냐?)
print(arr02)

arr03 = re.split("[\s]|[,]", str01)
print(arr03)

# join
arr04 = ['1','2','3','4']
print(arr04)
a = "+".join(arr04)
print(a)

print(eval(a))
 # eval 함수 - 웬만하면 안쓰는게 좋다. 입력값을 system path를 가지고와라 라고하면 진짜 가져와짐. 외부에서 컴퓨터 내부에 있는 무언가를 가지고 와질 수 있어. 안쓰는게 좋아.
 
 