def func1(a):
    x = 3
    return a + x

def func2(a):
    return a + x

def func3(a):
    global g
    g = 3
    return a + g

print(func1(3))
x = 1
print(func2(3))

print(func3(10))
print(g)

