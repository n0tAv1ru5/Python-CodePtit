import re

ans = list()


def find_numbers(input_string):
    numbers = re.findall(r"\d+", input_string)
    return numbers


for _ in range(int(input())):

    input_string = input()
    ans.extend(find_numbers(input_string))
ans = sorted(list(map(int, ans)))
print(*ans, sep="\n")
