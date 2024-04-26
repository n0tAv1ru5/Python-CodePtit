input()
nums_list = list()
while True:
    try:
        nums_list.extend(list(map(int, input().split())))
    except EOFError:
        break
even_list = sorted([x for x in nums_list if x & 1 == 0])
odd_list = sorted([x for x in nums_list if x & 1 == 1], reverse=True)
even_index = 0
odd_index = 0
for num in nums_list:
    if num & 1 == 1:
        print(odd_list[odd_index], end=" ")
        odd_index += 1
    else:
        print(even_list[even_index], end=" ")
        even_index += 1
print()
