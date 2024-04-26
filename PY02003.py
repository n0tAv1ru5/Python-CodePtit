def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 và 1 không phải là số nguyên tố

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


n = 100
primes = sieve_of_eratosthenes(n)
hamming = list()

for i in [1, 2, 3, 5]:
    for j in range(1, 1000):
        if j in [2, 3, 5] or j not in primes[3:]:
            hamming.append(i * j)
hamming = sorted(set(hamming))

for _ in range(int(input())):
    k = int(input())
    if k in hamming:
        print(hamming.index(k) + 1)
    else:
        print("Not in sequence")
