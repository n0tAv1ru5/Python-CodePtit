def count_factors(n):
    factor_count = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            factor_count[j] += 1
    return factor_count


factor_counts = count_factors(10007)

for _ in range(int(input())):
    x = int(input())
    curr_max = max(factor_counts[: x + 1])
    for idx, fac in enumerate(factor_counts[x + 1 :]):
        if fac > curr_max:
            print(idx + x + 1)
            break
