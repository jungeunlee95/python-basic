# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

# --- 1
a = []
for _ in range(5):
    a.append(int(input('> ')))
print(round(sum(a)/len(a),1))

# --- 2
result = 0
for _ in range(5):
    result += int(input('> '))
print(round(result/5, 1))