from itertools import permutations

for _ in range(int(input())):
    n = int(input()) + 1
    permutations_list = list(permutations([x for x in range(1, n)]))[::-1]
    print(len(permutations_list))
    for item in permutations_list:
        print("".join(map(str, item)), end=" ")
    print()