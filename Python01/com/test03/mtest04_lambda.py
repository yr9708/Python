# -*- coding:utf-8 -*-
# lambda function : 익명함수 -> 함수를 만들지 않고 (선언만 해두고) 필요할 때 바디를 만들어서 사용
from cProfile import label

#
hap01 = lambda a, b : a + b 
print(hap01(10,20))

gob = lambda a, b : a * b 
print(gob(30,40))

hap02 = lambda a, b, c : a + b + c
print(hap02(5,6,7))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
print(a)
a.sort(key=lambda i:i[2])
print(a)

min01 = (lambda x, y: x if x < y else y)(11,22) # 만일 x < y 가 참이면 x, 아니면 y
print(min01)

# x랑 y랑 입력하여 x가 y보다 크면 x, 아니면 y 리턴
max01 = (lambda x , y : x if x > y else y)(int(input('x : ')), int(input('y : ')))
print(max01)

b = lambda x : (lambda y : x + y)
c = b(100) # lambda y : 100 + y
d = c(90) # 100 + 90
print(d)
print(b(100)(90))

# 1 ~ 100 사이의 숫자 중 5의 배수를 출력하자
e = lambda x : bool(x % 5) # false , 왜냐면 5로 나눴을 때 0이 나오고 0이면 false니까
five = [i for i in range(1, 101) if not e(i)]
'''
five = []
for i in range(1, 101):
    if not e(i):
        five.append(i)
'''
print(five)

# None == null
f = lambda x : x if (x % 5 != 0) else None
result = [i for i in range(1,101) if not f(i)]
print(result)

result_five = [i for i in range(1, 101) if not (lambda x : x if(x % 5 !=0) else None)(i)]
print(result_five)