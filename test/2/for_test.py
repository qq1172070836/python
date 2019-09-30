total_num = 0
for i in range(0, 101):
    total_num += i
print(total_num)

for n in range(1, 10):
    print()
    for m in range(1, n+1):
        print('%dx%d=%d' % (m, n, n*m), end=' ')