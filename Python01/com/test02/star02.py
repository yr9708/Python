# -*- coding:utf-8 -*-
# 1
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))
'''
 \n을 조인할거야 ([안에 있는 것들을
 i가 0일 때는 별 하나가 찍혀서 ''.join 공백이랑 조인 됨
 i가 1 일 때는 별 하나 + 별 하나 가 만들어져서 ''.join 공백이랑 조인 됨
 
'''
# \n이랑 나머지가 조인 -> '\n'.join(['*','**','***','****','*****'])
# 나머지 : 리스트 값들이 있네
# ''.join(['*' for i in range(i+1)] for i in range(5)]

# 나머지 리스트 안에 있던 별들
# ''.join(['*' for i in range(i + 1)])
# i가 0 일 때 => ''.join(['*']) -> '*'
# i가 1 일 때 => ''.join(['*', '*']) -> '**'



# 2
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))
print('——')

# 3
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(i + 1)]) for i in range(5)]))
print('——')

# 4
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(5 - i)]) for i in range(5)]))
print('——')

# 5
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(2 * i + 1)]) for i in range(5)]))
print('——')