def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("mymod.py : 최상위 모듈(독립실행)시 출력된다!")

if __name__ == '__main__':
    main()
else:
    print('mymod.py의 모듈 이름 : ' + __name__)