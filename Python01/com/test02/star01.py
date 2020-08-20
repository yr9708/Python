# -*- coding:utf-8 -*-
'''
*
**
***
****
*****
'''
for i in range(1,6):
    print('*'*i)
print('--------')
for i in range(5):
    for j in range(i + 1):
        print('*',end=' ')
    print()
print('--------')
for i in range(5):
    print('*'*(i + 1))
'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    print('*'*i)
print('--------')
for i in range(5):
    print('*' * (5-i))
'''
    *
   **
  ***
 ****
*****

'''
print('--------')
for i in range(1,6):
    print(' '*(5-i),'*'*(i))
print('--------')
for i in range(5):
    print(' '*(4-i) + '*'*(i+1))
print('--------')
    
'''
*****
 ****
  ***
   **
    *
'''
for i in range(5,0,-1):
    print(' '*(5-i), '*'*i)
print('--------')
for i in range(5):
    print(' '*(i) + '*' * (5-i))
    
'''
     *
    ***
   *****
  *******
 *********
'''
for i in range(1,6):
    print(' '*(6-i),'*'*(i+(i-1)),' '*(5-i))
print('--------')

for i in range(5):
    print(' ' * (4 - i) + '*' * (2 * i + 1))
    
