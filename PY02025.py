input()

a = set((map(int, input().split())))
b = set((map(int, input().split())))
print(*sorted(a & b))
print(*sorted(a - b))
print(*sorted(b - a))
