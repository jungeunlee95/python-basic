class MyString:

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        return MyString(self.s + other.s)

    def __radd__(self, other):
        return other + self.s

    def __mul__(self, cnt):
        return self.s * cnt

s = MyString('Python Programmer is Good')
t = s / ' '
print(type(t))
print(t)

print('--------------------------------')
# print(s + " HaHa")
print(s + MyString(" HaHa"))
print(MyString("Hello") + MyString(" !!! ") + MyString("~~"))

print('Hello ' + MyString('World'))

print(MyString('Python')*3)
