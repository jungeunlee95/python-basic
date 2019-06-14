'''
call by reference 이지만,
내부에서 변경하더라도 변경되지 않는다. (immutable)
'''
def f(i):
    i = 20

a = 10
f(a)
print(a)


# 파라미터가 sequence type(immutable)인 경우 내부에서 변경시 오류
# a = (1, 2, 3) -> error
def f2(seq):
    seq[0] = 0

a = [1,2,3]  # -> 변경!
f2(a)
print(a)