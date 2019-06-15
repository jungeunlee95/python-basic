# 문제8.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
a = input('입력> ')

# --- 1
def reverse1(s):
    return s[::-1]
print(f'결과> {reverse1(a)}')

# --- 2
def reverse2(s):
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

print(f'결과> {reverse2(a)}')

# --- 3
reverse3 = lambda x : x[::-1]
print(f'결과> {reverse3(a)}')
