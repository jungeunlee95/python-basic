# While
count = 1
while count < 11:
    print(count, end=' ')
    count += 1
else:
    print('')

hap, i = 0, 1
while i <= 10:
    hap += i
    i += 1

print( '합: {0}'.format(hap))

print('--------------')
i = 0
while i < 10:
    i += 1
    if i < 5:
        continue
    print(i, end=' ')
    if i > 10:
        break
else:
    print('else block')

print('done')

print('--------------')
i = 0
while True:
    print(i)
    if i > 5:
        break
    i += 1


# for
print('------------ for문 -------------')
a = ['cat', 'cow', 'tiger']

for animal in a:
    print(animal)

for x in range(10):
    print(x, end=" ")
print()

print('-----------------------')

l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]

for data in l:
    print('이름:%s, 나이:%d' % data)

for name, age in l:
    print('이름:{0}, 나이:{1}'.format(name, age))
print('-----------------------')
l = ['red', 'orange', 'yellow', 'green', 'blue']
for index, color in enumerate(l):
    print(index, color)
print('-----------------------')
for i in range(10):
    if i > 5:
        break

    print(i, end=' ')
print()
print('-----------------------')
for i in range(10):
    if i <= 5:
        continue

    print(i, end=' ')
