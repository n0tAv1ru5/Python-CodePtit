while True:
    n = int(input())
    if n == 0:
        break
    nums_list = {int(input()) for _ in range(n)}
    if len(nums_list) == 1:
        print("BANG NHAU")
    else:
        print(min(nums_list), max(nums_list))