# # 문제6
# # 숨겨진 카드의 수를 맞추는 게임입니다.
# # 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# # 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게",
# # 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# # 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.
import sys
from random import randint

# ---- 1 : 함수 사용
# 게임 시작 함수
def start_game():
    global min_val, max_val, num, cnt
    print("수를 결정하였습니다. 맞추어 보세요.")
    num, min_val, max_val, cnt = randint(1, 100), 1, 100, 1

# 숫자 판별 함수
def check_val(i):
    global min_val, max_val
    if i > num :
        max_val = i
        print("더 낮게")
    elif i < num :
        min_val = i
        print("더 높게")
    else:
        return 1

num = min_val = max_val = cnt = 0

start_game()
while True:
    print(f"{min_val}-{max_val}")
    i = int(input(f'{cnt}>> '))
    cnt += 1

    if check_val(i) == 1:
        end = input("맞았습니다. \n다시하시겠습니까(y/n)>>")

        if end == 'y':
            start_game()
        else:
            if end != 'n': print("잘못 입력 하셨습니다.")
            break



# ---- 2 : 이중 while
while True:
    min_val, max_val, cnt = 1, 100, 1
    correct_num = randint(1, 100)
    print("수를 결정하였습니다. 맞추어 보세요.")

    while True:
        print(f'{min_val}-{max_val}')
        input_num = i = int(input(f'{cnt}>> '))
        cnt += 1

        if input_num == correct_num:
            end = input("맞았습니다. \n다시하시겠습니까(y/n)>>")
            if end != 'y':
                if end != 'n': print("잘못 입력하셨습니다.")
                sys.exit(1)
            break

        if input_num < correct_num:
            print('더 높게')
            min_val = input_num
        else:
            print('더 낮게')
            max_val = input_num

        input_num += 1
