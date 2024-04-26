n = int(input())
nums_list = sorted([int(input()) for _ in range(1, n)])
nums_list.append(int(0))
for i in range(1, n + 1):
    if nums_list[i - 1] != i:
        print(i)
        break
