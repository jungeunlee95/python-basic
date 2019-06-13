a = 20
print(not a < 30)
print(a < 30 and a != 30)
print(a == 30 or a > 30)

print('------')
b = 10
print(True + 1)
print((a < b) + 1)

print('------')
# 다른 타입의 객체도 bool 타입으로 변환이 가능하다
print(bool(10), bool(0))
print(bool(3.14), bool(0.))
print(bool('abc'), bool(''))
print(bool([1, 2, 3]), bool([]))
print(bool((1, 2, 3)), bool(()))
print(bool({1:2}), bool({}))
print(bool(None))

print('------')
# 논리식의 계산 순서
print([] or 'logical')
print('logical' and 'operator')
print(None and 1)
print('' and 1)

def f():
    print('execution !!!! ! !!! !!')
#if(1+2<10):
#    f()
1+2<10 and f()

print('-------')
s = 'hello world'
s and print(s)

print('-------')
def f(msg=None):
    msg and print(msg)
s = 'hello world'
f()
f("실행")








