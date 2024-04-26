for i in range(1, int(input()) + 1):
    str_1 = sorted(list(input()))
    str_2 = sorted(list(input()))
    print(f"Test {i}:", "YES" if str_1 == str_2 else "NO")