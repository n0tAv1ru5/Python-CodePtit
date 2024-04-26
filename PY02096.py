m, n = map(int, input().split())
L, R = map(int, input().split())
count = 0

for i in range(m, R + 1, m):
    flag = True
    if i >= L and str(n) in str(i):
        for idx, num in enumerate(str(i)[::-1], start=1):
            if num == str(n) and idx % 2 == 1:
                flag = False
                break
        if flag:
            count += 1

print(round(count % (1e9 + 7)))