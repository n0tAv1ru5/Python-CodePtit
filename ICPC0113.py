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


prime_list = sieve_of_eratosthenes(1000005)

for _ in range(int(input())):

    lim = int(input())

    for i in range(lim):
        k = int(str(i)[::-1])
        if k > i and k < lim and prime_list[i] and prime_list[k]:
            print(i, k, end=" ")
    print()
