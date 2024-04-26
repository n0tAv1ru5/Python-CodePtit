def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def count_numbers(L, R, N):
    is_prime = sieve_of_eratosthenes(N)
    count = 0
    count = sum(1 for x in is_prime[max(N, L):R] if x)

    return count


while True:
    LR = input()
    if LR == "-1":
        break
    L, R = map(int, LR.split())
    N = int(input())
    result = count_numbers(L, R + 1, N + 1)
    print(result)
