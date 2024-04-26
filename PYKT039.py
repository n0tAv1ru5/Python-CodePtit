for _ in range(int(input())):
    input()
    list_a = sorted(list(map(int, input().split())))
    list_b = sorted(list(map(int, input().split())))
    flag = 1
    for a, b in zip(list_a, list_b):
        if a > b:
            print("NO")
            flag = 0
            break
    if flag:
        print("YES")
