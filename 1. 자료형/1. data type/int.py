a = 23
print(type(a))
print(isinstance(a, int))

b = 0b1101
c = 0o23
d = 0x23

print(a, b, c, d)


# 3.x int와 long이 합쳐졌다. (무한대 표현 범위)
e = 2 ** 1024
print(e)
print(type(e))

# 변환변수
print(oct(38))
print(hex(38))
print(bin(38))