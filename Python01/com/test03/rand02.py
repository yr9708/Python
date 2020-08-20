# -*- coding:utf-8 -*-
import random

# 1부터 45 사이의 숫자 6개를 중복 없이 만들어서 list로 리턴하는 lotto() 함수를 만들자
# main 함수에서 호출하여 출력하자

def lotto():
    list = []
    for i in range(6):
        a = random.randint(1,45)
        if a not in list :
            list.append(a)
        else :
            b = random.randint(1,45)
            while b not in list:
                list.append(b)

    return list

if __name__ == '__main__':
    print(lotto())