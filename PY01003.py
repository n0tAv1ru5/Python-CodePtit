from math import log10

for _ in range(int(input())):
    n = int(input())
    i = 0
    if n <= 10:
        print(n)
    else:
        while n > 10**i:
            n = round(n, -i - 1)
            i+=1
            print(n)
