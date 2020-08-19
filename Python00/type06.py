# dictionary : 자바의 map이랑 똑같은 특징을 가진다. 1. 순서X, 2. 중복허용(value만)
# 생성자 사용
dict01 = dict()
dict01[1] = 'one'
dict01['two'] = 2
print(dict01)

# {}
dict02 = {}
dict02['one']=1
dict02[2]='two'
dict02[3] = 3
print(dict02)

# key를 통해 value값 가져와보자
print(dict01.get(1))
print(dict02['one'])
print(dict02.keys())
print(dict02.values())
print(type(dict02.keys()))
print(list(dict02.keys())[0])
