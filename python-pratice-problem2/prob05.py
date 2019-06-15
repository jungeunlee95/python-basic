# 문제5.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

# --- 1 : *args로 받기
def sum1(*args):
    result = 0
    for i in args:
        result += i
    return result
print(sum1(1,2,3,4,5,10))

# --- 2 : 입력 -> list로 변환해서 받기
def sum2(a):
    result = 0
    for i in list(a):
        result += int(i)
    return result
a = list(map(int, input("숫자를 여러개 입력하세요 : ").split()))
print(sum2(a))