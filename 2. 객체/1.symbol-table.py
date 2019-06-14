# 심볼 테이블 내용확인
g_a = 1
g_b = '둘리'

def f():
    l_a = 2
    l_b = '마이콜'
    print("@@", locals())

for i in range(10):
    g_c = 3
    g_d = 'python'
    print("##", locals())

f()
print("^^", globals())

print('----------------------------------------------------------------')
print('-----------1. 정의된 함수 -----------')
f.k = 'hello'
f.haha = "haha!!!"
print("f.haha : ", f.haha)
print("f.__dict__ : ", f.__dict__)


print('-----------2. 클래스 객체 -----------')
class MyClass:
    x = 10
    y = 20
g_a = 1

MyClass.z = 10
print("MyClass.__dict__ : ", MyClass.__dict__)

# 내장 함수는 심볼 테이블이 아니라 확장 불가능
# print.z = 10
# print(print.__dict__)

# 내장 클래스는 심볼테이블이 맞지만 확장 불가능
# str.z = 10
# print("str.__dict__ : ", str.__dict__)


# 내장 클래스로 생성된 객체는 심볼테이블 x 확장 불가능
# print("g_a : ", g_a)  # 1
# print("g_a.__dict__  : ", g_a.__dict__)  : error

print('----------------------')
# 사용자 정의된 클래스로 생성된 객체는 심볼테이블 O -> 확장O
o = MyClass()
o.z = 10
print(o.__dict__)















