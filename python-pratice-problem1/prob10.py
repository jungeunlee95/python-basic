'''
문제10
숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
- 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
    - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )
'''

# --- 1
num = int(input('숫자를 입력하세요 : '))
result = 0
if num % 2 == 0:
    for i in range(num+1):
        if i % 2 == 0 : result += i
else :
    for i in range(num+1):
        if i % 2 == 1 : result += i

print(f'#1 결과 값 : {result}')

# --- 2
def sum1(x):
    result = 0
    for i in range(num+1):
        if i % 2 == x : result += i
    return result

print(f'#2 결과 값 : {sum1(0) if num % 2 == 0 else sum1(1)}')


# --- 3
s = 0
for n in range(num+1):
    if num & 0x0001 ^ n & 0x0001 == 0:
        s += n
print(f'#3 결과 값 : {s}')









