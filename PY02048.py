import bisect

n, k = map(int, input().split())
nums_list = sorted(list(map(int, input().split())))
count = 0
idx = 0
for a, b in zip(nums_list, nums_list[1:]):
    idx += 1
    if b - a > k:
        count += 1
if idx < n:
    count += 1
print(count)
