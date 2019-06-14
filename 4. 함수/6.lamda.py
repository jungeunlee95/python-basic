def f(x):
    return x * 2

for i in range(10):
    print(f'{i}:{f(i)}', end=' ')
print()

print('----------------------------')
for i in range(10):
    print(f'{i}:{(lambda x : x*2)(i)}', end=' ')
print()

print('----------------------------')
import re

states = ['Alabama', '  Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_strings(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results

results = clean_strings(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s))
print(results)

print((lambda x,y: x + y)(10, 20))









