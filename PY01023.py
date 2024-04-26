def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


for _ in range(int(input())):
    n = int(input())
    factors = prime_factorization(n)
    print(f"1 ", end="")
    for nums in sorted(set(factors)):
        print(f"* {nums}^{factors.count(nums)}", end=" ")
    print()
