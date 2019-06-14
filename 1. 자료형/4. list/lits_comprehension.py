print('-------------- 기본 ------------------')
results = []
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = i * i
    results.append(result)
print(results)

results = [result*result for result in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(results)

print('------------ if -------------------')

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = [s for s in strings if len(s) <= 2]
print(strings)

print('---------------- 짝수 list -----------------')

evens = [i for i in range(1, 101) if i % 2 == 0]
print(evens)

print('----------------3 6 9 list-----------------')
gugudan = [(i, '짝'*(str(i).count('3')+str(i).count('6')+str(i).count('9'))) for i in range(1, 101) if str(i).count('3') != 0 or str(i).count('6') != 0 or str(i).count('9') != 0]
print(gugudan)

print('-------------- set -----------------')

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = [len(s) for s in strings]
print(lens)

lens = {len(s) for s in strings}
print(lens)

print('--------------- dict -----------------')
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
dicts = {s: len(s) for s in strings}
print(dicts)






