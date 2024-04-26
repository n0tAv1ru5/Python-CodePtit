import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

input()
input_nums = list(map(int, input().split()))

prime = sorted([x for x in input_nums if is_prime(x)])
prime_idx = 0

for idx, val in enumerate(input_nums):
    if is_prime(val):
        input_nums[idx] = prime[prime_idx]
        prime_idx += 1
        
print(*input_nums)
