# 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
num = input('수를 입력하세요 : ')

if num.isalpha():
    print('정수가 아닙니다.')
else :
    num = int(num)

    # --- 1
    print('짝수' if num % 2 == 0 else '홀수')

    # --- 2
    print('짝수' if num & 0x0001 == 0 else '홀수')
