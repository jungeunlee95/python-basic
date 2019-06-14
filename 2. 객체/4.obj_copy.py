import copy

a = 1
b = a

a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)

print('------ swallow copy(얕은 복사) ------')
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.copy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

x[0] = 'change'
y[0] = 'xxxxxx'
print(x)
print(y)


print('------ deep copy(깊은 복사) ------')
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.deepcopy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

x[0] = 'change'
y[0] = 'xxxxxx'
print(x)
print(y)

print('------ 얕은 복사 ------')
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

print('------ 깊은 복사 ------')
a = ['hello', 'world']
b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])

