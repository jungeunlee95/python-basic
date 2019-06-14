import sys

x = object()
print(type(x))
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))

print('--------레퍼런스 값 줄이기---------')
print("before : ", globals())
del x
print(sys.getrefcount(y))
print("after : ",globals())