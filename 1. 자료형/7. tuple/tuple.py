# 튜플 생성
t = ()      # 공튜플
t = (1,)    # 항목이 하나일 때는 반드시 ,(콤마) 사용
print(t, type(t))
t = (1, 2, 3)
print(t, type(t))

print("----sequence 연산-----")
# sequence 연산
# 인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

# 슬라이싱
print(t[1:3])
print(t[::-1])

# 반복
print(t*2)

# 연결
print(t + (99,))

# 확인
print(4 not in t)

# immutable
# t[0] = (100,)
# print(t)

print("----swap-----")
# 여러개 값 대입
x, y, z = (10, 20, 30)
print(x, y, z)

# swap
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)


# 객체함수
print("-------객체함수---------")
t = (1, 2, 3)

s = set(t)
print(s, type(s))

l = list(s)
print(l, type(l))

t = tuple(l)
print(t, type(t))

# packing : tuple만 가능
print("-------packing---------")
t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking
print("-------unpacking---------")
a, b, c, d = t
print(a, b, c, d)

# error
# a, b, c = t
# a, b, c, d, e = t

print("----확장 언패킹------")
t = (1, 2, 3, 4, 5, 6)
a, *b = t
print(a,  b)

*a, b = t
print(a, b)

a, b, *c = t
print(a, b, c)

a, *b, c = t
print(a, b, c)

print("---------------")
# cf, 여러개 파라미터 받는 함수
def sum1(*num):
    return sum(num)
print(sum1(1, 2, 3, 4))

print("-------printf---------")
# c의 printf() 함수 흉내
def printf(str, *a):
    print(str % a)
printf("name : %s, age: %d", "둘리", 10)