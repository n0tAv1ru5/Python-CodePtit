from math import gcd


def split_list(input_list, n):
    return [input_list[i : i + n] for i in range(0, len(input_list))]


def find_gcd(input_list):
    result = input_list[0]
    for num in input_list[1:]:
        result = gcd(result, num)
    return result


for _ in range(int(input())):
    n, k = map(int, input().split())
    input_list = list(map(int, input().split()))
    flag = 1
    for i in range(1, len(input_list) + 1):
        sep_list = split_list(input_list, i)
        for sub_list in sep_list:
            if find_gcd(sub_list) == k:
                print(i)
                flag = 0
                break
        if not flag:
            break
    if flag:
        print("-1")
