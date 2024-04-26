from itertools import product

check = frozenset({2, 3, 5, 7})

for i in range(4, int(input()) + 1):
    combinations_of_check = product(check, repeat=i)

    for combination in combinations_of_check:
        str_com = "".join(map(str, combination))
        if set(combination) == check and str_com[-1] != "2":
            print(str_com)
