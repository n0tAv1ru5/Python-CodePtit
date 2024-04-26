n = int(input())
width = len(str(n-1))
for i in range(n):
    for j in range(n):
        if abs(i - j) < 10:
            print(str(abs(i - j)).rjust(width," "), end=" ")
        else:
            print(abs(i - j), end=" ")
    print()
