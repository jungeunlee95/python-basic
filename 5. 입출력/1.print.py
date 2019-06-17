import sys

print(1)
print('hello', 'world')

# sep 파라미터
x = 0.2
s = 'hello'
print(str(x) + ' ' + s)
print(x, s, sep=' ')

# 기본적인 print() 함수 호출
print(sep=' ', end='\n')

# file 파라미터 지정
print('Hello World', file=sys.stdout)
print('error : hello world', file=sys.stderr)

print('--------------------')
f = open('hello.txt', 'w')
print(type(f))
print('hello world', file=f)
f.close()

# 참고
sys.stdout.write('heloo~~ world!!!!')