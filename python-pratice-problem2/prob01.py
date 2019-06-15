s = '/usr/local/bin/python'
a = s.split('/')

# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
# --- 1 : if, else 사용
for i in range(1, len(a)) :
    if i!=len(a)-1:
        print(f'\'{a[i]}\'', end=', ')
    else:
        print(f'\'{a[i]}\'')

# --- 2 : 한줄 if, else 사용
for i in range(1, len(a)):
    print(f'\'{a[i]}\'', end='\n' if i==len(a)-1 else ', ')

# --- 3 : 논리 연산자 사용
for i in range(1, len(a)) :
    i!=len(a)-1 and print(f'\'{a[i]}\'', end=', ')
    i==len(a)-1 and print(f'\'{a[i]}\'')

# --- 4 : split() 사용
lst = s.split('/')
r = '\', \''.join(lst[1:])
print('\'' + r + '\'')

print('------------------------------------')


# 문제2. 디렉토리 경로명과 파일명을 분리하여 출력하세요.
# --- 1 : if, else 사용
dir_name = ''
file_name = ''
for i in range(1, len(a)):
    if i==len(a)-1:
        file_name = a[i]
    else:
        dir_name += '/' + a[i]
print(f'\'{dir_name}\', \'{file_name}\'')

# --- 2 : rsplit() 사용
r = '\', \''.join(s.rsplit('/', 1))
print('\'' + r + '\'')
