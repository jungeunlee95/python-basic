# 리스트 생성과 연산
l = [1, 2, 'python']

print(l[-2], l[-1], l[0], l[1], l[2])
print(l[1:3])
print(l * 2)
print(l + [3, 4, 5])
print(len(l))
print(2 in l)

del l[0]
print(l)

print('------리스트는 변경 가능(Mutable)한 자료형-------')
# 리스트는 변경 가능(Mutable)한 자료형
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

print('------슬라이싱을 통한 치환-------')
# 슬라이싱을 통한 치환
a = [1, 12, 123, 1234]

a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

a[2:3] = [30]
print(a)

print('------슬라이싱을 통한 삭제-------')
# 삭제
a = [1, 12, 123, 1234]
a[1:2] = [ ]
print(a)
a[0:] = [ ]
print(a)

print('------슬라이싱을 통한 삽입-------')
# 삽입
a = [1, 12, 123, 1234]

a[1:1] = ['a']
print(a)

a[5:] = [12345]
print(a)

a[:0] = [-12, -1, 0]
print(a)

# 중간
a[1:1] = ['a']
print(a)

# 마지막
a[5:] = [12345]
print(a)

# 처음
a[:0] = [99]
print(a)

# 여러개
a[2:2] = [222, 222, 222]
print(a)


print('------객체 함수-------')
# 객체 함수
a = [1, 1, 12, 123, 1234]

# 삽입
a.insert(1, 'a')
print("insert : ", a)

a.append(5)
print("append : ",a)

# 카운트
print("count : ", a.count(1))

# reverse
a.reverse()
print("reverse : ",a)

# 제거
a.remove('a')
print("remove : ",a)

# 정렬
a.sort()
print("sort : ", a)

# 확장
a.extend([6, 7, 8])
print("extend : ", a)


print("-------stack-------")
# 스택
stack = [ ]

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

print("-------queue-------")
# 큐
q = [ ]

q.append(100)
q.append(200)
q.append(300)

print(q)

print(q.pop(0))
print(q.pop(0))

print(q)



# sort
print('------sort------')

l = [1, 5, 3, 9, 8, 4, 2]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

print('------sort key------')
l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key=str);
print(l)

l.sort(key=int);
print(l)

# cf. 내장(전역)함수 sorted
print('------sorted------')
l3 = [10, 2, 22, 9, 8, 12, 14]
l4 = sorted(l3)
print(l4)

l4 = sorted(l3, reverse=True)
print(l4)

print('------sorted key------')
l3 = [10, 46, 22, 93, 81, 35, 44]
def f(n):
    return n % 10
l4 = sorted(l3, key=f)
print(l4)




