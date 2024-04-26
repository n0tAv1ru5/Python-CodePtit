for _ in range(int(input())):
    lim = int(input())

    for i in range(22, lim, 2):
        if str(i) == str(i)[::-1] and set(list(str(i))) <= {"0", "2", "4", "6", "8"} and len(str(i)) % 2 == 0:
            print(i, end=" ")
    print()
