print('---- 기본 인수값 ----')
def incr(a, step=1):
    return a + step

print(incr(10))
print(incr(10,2))

print('--------')

def decr(step=1, a=0):
    return a + step

print(decr(step=3))
print(decr(a=3))
print(decr(6, 7))

print('---- 키워드 인수 ----')
def area(width, height):
    return width + height

print(area(10, 20))
print(area(width=10, height=20))
print(area(height=10, width=20))

# 오류
# area(20, width=30)

print('---- 가변 인수 ----')
def vargs(a, *args):
    print(a, args)

vargs(10)
vargs(10,1)
vargs(10,2,3,4)

print("---- print 함수 ----")
def _print(*args, end='\n'):
    print(f'{end}'.join(args))

_print("#1 Hello", "Python")
_print("#2 Hello", "Python", end="\t")

print("---- printf 함수 ----")
def printf(format, *args):
    print(format % args)
printf("%s이 %d원짜리 %s를 입고있다", "정은", 5000, "드레스")

print("---- 정의되지 않은 키워드 인수 처리하기 ----")
def f(width, height, **kw):
    print("w, h : ", width, height)
    print("kw : ", kw)

f(10, 20)
f(10, 20, depth=10)
f(10, 20, depth=10, dimension=3)

print('-----------------------')
def g(a, b, *args, **kw):
    print("a, b : ",a, b)
    print("args : ",args)
    print("kw : ",kw)

print('---------- 1 --------')
g(10, 20)
print('---------- 2 --------')
g(10, 20, 30)
print('---------- 3 --------')
g(10, 20, c=60)
print('---------- 4 --------')
g(10, 20, 30, 40, 50, c=60, d=70)


print('-------- 튜플/사전 파라미터 --------')
def h(name, age, height):
    print(name, age, height)

h('둘리', 10, 150)

t = ('둘리', 10, 50)
h(t[0], t[1], t[2])
h(*t)

print('---------------------------------')
d = {'name':'둘리', 'age':10, 'height':150}
h(d['name'], d['age'], d['height'])
h(**d)