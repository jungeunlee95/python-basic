f = open('test.txt','rt',encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('---', text, '---')


print('-----------------')
# position 단위는 byte
pos = f.tell() # 현재 position
print(pos)     # 전체 파일 size = 35니까 36이면 다읽고 그 다음 위치겠네


print('------- seek --------')
# 1st parameter : offset
# 2nd parameter : from_what(0:파일시작, 1:현재위치, 2:끝)
# text mode에서는 from_what은 0(파일시작)만 허용
# 예외는 f(0, 2) 끝으로 이동하는 경우
f.seek(16, 0)
text = f.read()
print(text)

# 예외: seek(0, 2) 끝으로 이동하는 경우
f.seek(0,2)

# line 단위로 읽기
print('-------- readline() ---------')
line_num = 0
f2 = open('3.fileio2.py', 'rt', encoding='utf-8')
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    line_num += 1
    print(f'{line_num} : {line}', end='')

print('-------------- readlines() --------------')
f3 = open('3.fileio2.py', 'rt', encoding='utf-8')
lines = f3.readlines()
f3.close()
print(type(lines))
for line_num, line in enumerate(lines) :
    print(f'{line_num} : {line}', end='')



# with ~as
print('-------- with ~as ---------')
with open('3.fileio2.py', 'rt', encoding='utf-8') as f2:
    for line_num, line in enumerate(f2.readlines()):
        print(f'{line_num} : {line}', end='')