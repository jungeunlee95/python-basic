a = {1, 2, 3}
print(a, type(a))

print(len(a))
print(2 in a)
print(2 not in a)

print("--------------")
nums = [1, 2, 3, 2, 2, 4, 5, 6, 5, 6]
s = set(nums)
print(s)
nums = list(s)
print(nums)

# 객체 함수
print("---------객체함수------")
print(s)
s.add(4)
print(s)
s.add(1)
print(s)
s.discard(2)
print(s)
s.remove(3)
print(s)
s.update({2, 3})
print(s)
s.clear()
print(s)
s.add(3)
print(s)


# 수학 집합 관련 객체 함수
print("---------수학 집합 관련 객체 함수------")
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)                  # 합집합
print(s3)

s3 = s1.intersection(s2)           # 교집합
print(s3)

s3 = s1.difference(s2)             # 차집합
print(s3)

s3 = s1.symmetric_difference(s2)   # 교집합의 여집합?
print(s3)

s4 = {1}
print(s1.issubset(s4))             # F
print(s4.issubset(s1))             # T









