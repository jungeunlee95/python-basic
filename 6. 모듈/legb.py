# 네임스페이스가 주어지지 않은 변수나 함수는 LEGB 규칙에 따라 찾게 된다.
# 1. local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Built-in

a = 1 # G
def f():
    b = 200 # E
    print("f() a : ", a)
    def g():
        b = 100 # L
        print("g() b : ", b)
        print("g() __name__ : ", __name__)
    g()
    print("f() b : ", b)
    pass

if __name__ == '__main__':
    f()