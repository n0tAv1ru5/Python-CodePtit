def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p**2 <= n:
        if prime[p] == True:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1

    return prime


prime_list = sieve_of_eratosthenes(1000000)

for _ in range(int(input())):
    ans = 0
    lim = int(input())
    for i in range(2, lim - 6):
        if prime_list[i] and prime_list[i + 2] and prime_list[i + 6]:
            ans += 1
        if prime_list[i] and prime_list[i + 4] and prime_list[i + 6]:
            ans += 1
    print(ans)