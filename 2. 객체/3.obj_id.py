import sys

i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))

i1 = 11
i2 = 10 + 1
print(hex(id(i1)), hex(id(i2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

print('---------is-----------')
print(i1 is i2)
print(s1 is s2)

print('---------()-----------')
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(sys.getrefcount(t1), sys.getrefcount(t2))
print(t1 is t2)

print('---------tuple()-----------')
t3 = tuple(range(1,4))
print(sys.getrefcount(t3))
print(t1 is t3)

print('---------slicing-----------')
t4 = (0,1,2,3)[1:]
print(t1 is t4)
print(t3 is t4)





