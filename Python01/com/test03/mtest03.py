# -*- coding:utf-8 -*-
# 1. for 문을 사용하여 구구단을 전체 출력하는 함수 gugu()를 작성하고 main 함수에서 호출 하자
# 2. while문을 사용하여 구구단 중 파라미터로 전달 된 단만 출력하는 함수 guugdan(x)를 작성하고
#     main 함수에서 콘솔을 통해 n을 입력받아 호출 하자

def gugu():
    for i in range(2,10):
        print('<<%d단>>'% i)
        for j in range(1,10):
            # print('{} * {} = {}'.format(i, j, i*j))
            print('%d * %d = %d' %(i, j, i*j))

            # pass 함수에 아직 아무것도 안해놨을 때!

def gugudan(x):
    '''
        for j in range(1,10):
            print('{} * {} = {}'.format(x, j, x*j))
    '''      
    print('<'+str(x) +'단>')
    # print('<<', x, '단>>')
    i = 1
    while i <=9 :
        print('{} * {} = {}'.format(x, i, x*i))
        i += 1
            


if __name__ == '__main__':
    gugu()
    print('--------')
    gugudan(int(input('n 입력 : ')))