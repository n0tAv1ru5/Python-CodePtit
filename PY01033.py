from math import gcd

l, r = map(int, input().split())

for i in range(l, r - 1):
    for j in range(i, r):
        for k in range(j, r + 1):
            if gcd(i, j) == gcd(j, k) == gcd(i, k) == 1:
                print(f"({i}, {j}, {k})")
