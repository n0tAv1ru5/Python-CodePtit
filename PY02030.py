import math

check = 1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
input_nums = list(map(int, input().split()))

uniq = []
for num in input_nums:
    if num not in uniq:
        uniq.append(num)

for i, _ in enumerate(uniq):
    if is_prime(sum(uniq[: i + 1])) and is_prime(sum(uniq[i + 1 :])):
        print(i)
        check = 0
        break
if check:
    print("NOT FOUND")
