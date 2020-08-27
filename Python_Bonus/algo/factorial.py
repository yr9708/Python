# -*- coding:utf-8 -*-

# n! = n * (n-1) * (n-2) * ...* 2 * 1
def factorial(n):
    result = 1
    i = 1
    for i in range(n):
        result += result * i
        i += 1
    return result
# 강사님 코드
"""
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
"""

# 재귀함수
def factorialRecursion(n):
    if (n > 1):
        return n * factorialRecursion(n-1)
    else :
        return 1
# 강사님 코드
'''
def factorialRecursion(n):
    if n == 1:
        return 1
    return n * factorialRecursion(n-1)
    

'''

if __name__ == '__main__':
    n = int(input('input n : '))
    print('{} factorail = {}'.format(n, factorial(n)))
    print('{} factorail = {}'.format(n, factorialRecursion(n)))
    