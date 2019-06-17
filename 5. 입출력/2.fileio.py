# textmode 가 default : t
f = open('test.txt', 'w', encoding='utf-8')
write_size = f.write('안녕하세요\n파이썬입니다.')
f.close()
print(write_size)

# binary mode : b
f = open('test2.txt', 'wb')
write_size = f.write(bytes('안녕하세요\n파이썬입니다.', encoding='utf-8'))
f.close()
print(write_size)

print('--------read----------')
# read test
f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)

print('--------copy file--------')
# binary read : copy file
fsrc = open('python.png', 'rb')
data = fsrc.read()
fsrc.close()
print(type(data))

fdest = open('python2.png', 'wb')
fdest.write(data)
fdest.close()