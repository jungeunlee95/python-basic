d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d))

print(d['basketball'])

# 변경가능
d['volleyball'] = 6
print(d)

# 길이
print(len(d))

# in, not in by key
print('soccer' in d)
print('volleyball' not in d)


print("----------다양한 dict 객체 생성 방법----------")
d = dict()   # empty dict
print(d)

d = dict(one=1, two=2)  # keyword arguments
print(d)

d = dict([('one', 1), ('two', 2)])   # tuple list
print(d)

keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)

print("----------다양한 key 타입----------")
# key : immutable만 가능
d = {}
d[True] = 'ture'
d[10] = '10'
d['twenty'] = 20
#d[[1,2,3]] = '6' # error
print(d)

print("----------key 객체----------")
keys = d.keys()
print(keys, type(keys))
for key in keys:
    print(f"{key} : {d[key]}")

print("----------values 객체----------")
values = d.values()
print(values, type(values))

print("----------items 객체----------")
items = d.items()
print(items, type(items))


print("----------dict 복사----------")
phone = {
    '둘리' : '000-0000-0000',
    '마이콜' : '000-1111-1111',
    '또치' : '000-2222-2222'
}

p = phone
print(p)
print(phone)

p['도우넛'] = '000-3333-3333'
print(p)
print(phone)

print("-------- copy() --------")
p = phone.copy()
print(p)
print(phone)

p['또리'] = '000-4444-4444'
print(p)
print(phone)

print("-------- get() --------")
print(phone.get("도우넛"))
print(phone.get("또리"))
print(p.get("또리"))


print("-------- setdefault()--------")
print(phone.setdefault("둘리", "99"))
print(phone)
print(phone.setdefault("또리", "000-4444-4444"))
print(phone)

print("-------- 삭제+values --------")
number = phone.pop('둘리')
print(number)
print(phone)

print("-------- 튜플로 가져오기 popitem --------")
item = phone.popitem()
print(item)
print(phone)

print("-------- update --------")
phone.update({
    '도우넛' : '999-9999-9999',
    '바보' : '00'
})
print(phone)

print("-------- 모두 삭제 --------")
phone.clear()
print(phone)