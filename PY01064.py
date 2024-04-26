for _ in range(int(input())):
    n, k = map(int, input().split())
    string = "A"
    if n == 1 or k == 1:
        print("A")
        continue
    for i in range(66, 66 + n - 1):
        string = string + chr(i) + string
    print(string[k - 1])
