input()

a = sorted(set(list(map(int, input().split()))))
b = sorted(set(list(map(int, input().split()))))
print("YES" if a == b else "NO")