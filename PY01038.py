for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n % 7 != 0:
        n = n + int(str(n)[::-1])
        cnt += 1
        if cnt > 1000:
            n = -1
            break
    print(n)
