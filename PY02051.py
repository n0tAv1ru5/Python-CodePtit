n = int(input())
a, b = [[0]] * n, []
s = 0
for i in range(n) :
    a[i] = [int(x) for x in input().split()]
    b.append(sum(a[i]))
    s += b[-1]
if n == 2 :
    for i in b :
        print(int(i / 2), end = ' ')
else :
    s = int(s / 2 / (n - 1))
    for i in b :
        print(int((i - s) / (n - 2)), end = ' ')


