def count_divisors(num):
    divisors = [0] * (num + 1)
    for i in range(1, num + 1):
        for j in range(i, num + 1, i):
            divisors[j] += 1
    return divisors


divisor_counts = count_divisors(int(input()))
print(sum(1 for item in divisor_counts if item == 9))
