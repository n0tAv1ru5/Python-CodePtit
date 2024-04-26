def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


ans = 0
for _ in range(int(input())):
    ans += sum(prime_factorization(int(input())))
print(ans)
