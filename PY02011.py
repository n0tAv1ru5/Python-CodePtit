input()
nums_list = list(map(int, input().split()))
ans = 10e9
for num in nums_list:
    curr_gap = 0
    for num_al in nums_list:
        curr_gap += abs(num - num_al)
    if curr_gap < ans:
        ans = curr_gap
        chosen_element = num
print(ans, chosen_element)

