'''
구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
프로그램은 정답 여부를 다시 출력합니다.
'''
import random
import sys

# random 숫자 뽑기
a = random.randint(2,9)
b = random.randint(2,9)

print(f'{a} x {b} = ?\n')

# random list만들고 섞기
result = [str(random.randint(2,9)* random.randint(2,9)) for _ in range(8)] + [str(a*b)]
random.shuffle(result)

# 9개의 보기 출력
for i in range(len(result)):
    print(result[i], end='\t')
    if i ==2 or i == 5 or i == 8 :
        print()

# 정답 입력받기
answer = input('\nanswer : ')

# 문자입력하면 ㅃㅃ
if answer.isdigit() == False:
    print("숫자를 입력해주세요!")
    sys.exit(1)

# 정답인가
if int(answer) == a*b:
    print("\n정답")
else: print("\n오답")
