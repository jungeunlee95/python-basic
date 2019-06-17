f = open('123.txt', 'wb')
f.write(b'0123456789')
f.close()

f = open('123.txt', 'rb')
print("1 : ", f.tell())

f.seek(5, 1)
data = f.read(2)
print("2 : ", data)

f.seek(-5, 1)
data = f.read(3)
print("3 : ", data)

f.seek(0, 2)
data = f.read(3)
print("4 : ", data)