# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

# --- 1 : 직접 판단
a = ['3', '6', '9']
for i in range(1, 100):
    cnt = 0
    for j in str(i):
        if j in a :
            cnt += 1
    if cnt > 0: print(f'{i} {"짝"*cnt}')

# --- 2 : 직접 판단(함수, java st)
def check369(num):
    x = num // 10
    y = num % 10
    cnt = 0
    if x == 3 or x == 6 or x == 9 :
        cnt += 1
    if y == 3 or y == 6 or y == 9 :
        cnt += 1
    if cnt != 0 : print(f'{num} {"짝"*cnt}')

for num in range(1,100):
    check369(num)

# --- 3 : count() 사용
for i in range(1, 100):
    num = str(i)
    c = num.count('3') + num.count('6') + num.count('9')
    if c > 0:
        print(f'{num} {"짝"*c}')


