max_length = 0
current_length = 0

n = int(input())
nums_list = list(map(int, input().split()))
k = max(nums_list)

for num in nums_list:
    if num == k:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
print(max_length)
