def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


input()
a = list(map(int, input().split()))
b = list()
b.extend(x for x in a if x not in b)
flag = 1
for idx in range(1, len(b)):
    if is_prime(sum(b[:idx])) and is_prime(sum(b[idx:])):
        print(idx -1)
        flag = 0
        break
if flag:
    print("NOT FOUND")
