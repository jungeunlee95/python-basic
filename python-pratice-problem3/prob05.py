'''
문제5.
선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여
다음과 같은 출력이 되도록 완성하는 문제입니다.

'''
# --- 1 : 그냥 정렬
a = [5, 9, 3, 8, 60, 20, 1]
print(f'Before sort \n{" ".join(map(str,a))}')

for i in range(len(a)):
    for j in range(i+1, len(a)-1):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(f'After sort \n{" ".join(map(str,a))}')



# --- 2 : lambda
print('-------------------------------------')
a = [5, 9, 3, 8, 60, 20, 1]
print(f'Before sort \n{" ".join(map(str,a))}')

def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            a[j], a[j + 1] \
                = (lambda x, y: [x, y] if x > y else [y, x]) (a[j], a[j + 1])
    return a

print(f'After sort \n{" ".join(map(str,bubblesort(a)))}')
