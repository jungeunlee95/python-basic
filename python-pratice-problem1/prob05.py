# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요
a = list(range(1,50))
sum1 = cnt = 0

for i in a:
    if(i%3==0):
        cnt+=1
        sum1+=i

print(f'주어진 리스트에서 3의 배수의 개수 => {cnt}')
print(f'주어진 리스트에서 3의 배수의 합 => {sum1}')
