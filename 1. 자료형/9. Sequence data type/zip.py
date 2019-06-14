# set 은 순서 X
# seq1 = {'foo', 'bar', 'baz'}
# seq2 = {'one', 'two', 'three'}

# list 순서 ㅇㅇ
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
z = zip(seq1, seq2)
print(z)
print(type(z))

print(' -------------------------------- ')

for t in z:
    print(t, type(t))

print(' -------------------------------- ')

z = zip(seq1, seq2)

for idx, (a, b) in enumerate(z):
    print('%d: %s, %s' % (idx, a, b))

print(' -------------------------------- ')

d1 = [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]

seq1, seq2 = zip(*d1)
print(seq1)
print(seq2)

