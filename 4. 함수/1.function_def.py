def dummy():
    pass

def my_function():
    print('Hello World')

def times(a, b):
    return a * b

def none():
    return

dummy()
my_function()
print(times(10, 10))
print(none())

print('----- 함수도 객체다 ------')
print(dummy, type(dummy))
f = my_function
f()

print(f, my_function)

print('----- 여러 return 값 -> tuple로 packing ------')
def func():
    return 10, 'hello', {1, 2, 3}, (1, 2, 3)
print(func())