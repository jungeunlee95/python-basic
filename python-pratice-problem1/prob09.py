# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴: ')
menupan = {'오뎅' : 300, '순대' : 400, '만두' : 500}

print(f'가격 : {menupan[menu] if menu in menupan else 0}')
