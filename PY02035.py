import textwrap
from collections import Counter

check = 1

input_str = input()
n = int(input())

sub_strings = list(textwrap.wrap(input_str, 2))
counter_result = Counter(sub_strings)
ans = []

for item in counter_result.items():
    if item[1] >= n:
        check = 0
        ans.append(item)
        
for item in sorted(ans):
    print(*item, sep=" ")

if check:
    print("NOT FOUND")