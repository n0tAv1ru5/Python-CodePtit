import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = input()
    sum_digits = sum(list(map(int, list(n))))
    if is_prime(int(n)) and is_prime(sum_digits) and is_prime(int(n[::-1])):
        print("Yes")
    else:
        print("No")
