n = int(input())
nums_list = list()

while len(nums_list) < n:
    nums_list.extend(list(map(int, input().split())))
exc_list = [x for x in range(1, max(nums_list) + 1)]

if nums_list == exc_list:
    print("Excellent!")
else:
    for num in exc_list:
        if num not in nums_list:
            print(num)