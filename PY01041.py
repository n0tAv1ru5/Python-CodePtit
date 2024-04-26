def inc_dec_check(n):
    for i in range(1, len(n)):
        if int(n[i]) == int(n[i - 1]) or len(n) < 3 or i == len(n) - 1:
            return False
        if int(n[i - 1]) < int(n[i]) and int(n[i + 1]) < int(n[i]) :
            if list(n[i:]) == sorted(list(n[i:]), reverse=True) and len(n[i:]) == len(set(list(n[i:]))):
                return True
            else:
                return False


for _ in range(int(input())):
    n = input()
    print("YES" if inc_dec_check(n) else "NO")