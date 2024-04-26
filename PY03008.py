from collections import Counter

points_list = list()

n = int(input()) - 1
for _ in range(n):
    points_list.extend(list(map(int, input().split())))

counter = Counter(points_list)

count_set = set()

for _, val in counter.items():
    count_set.add(val)
if len(count_set) != 2:
    print("No")
else:
    print("Yes")
