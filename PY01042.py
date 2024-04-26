for _ in range(int(input())):
    n = set(list(input()))
    print("YES" if n <= {"0", "1", "2"} else "NO")