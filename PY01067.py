def int_to_ternary(n):
    if n == 0:
        return "0"
    ternary = ""
    while n > 0:
        remainder = n % 3
        ternary = str(remainder) + ternary
        n //= 3
    return ternary


for _ in range(int(input())):
    n = int(input())
    i = 2
    while n > 0:

        ternary_number = int_to_ternary(i)
        if str(ternary_number).count("2") > len(str(ternary_number)) / 2:
            print(ternary_number, end=" ")
            n -= 1
        i += 1
    print()