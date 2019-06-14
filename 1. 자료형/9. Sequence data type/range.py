seq = range(10)
print(seq, type(seq))
print(list(seq[5:]))
print(len(seq))

for i in seq:
    print(i, end = ' ')
else:
    print()

seq2 = range(5, 16, 5)
for i in seq2:
    print(i, end = ' ')
else:
    print()

seq3 = range(0, -10, -1)
for i in seq3:
    print(i, end = ' ')
else: print()
