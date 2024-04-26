line_1 = set(map(lambda x :x.lower(), input().split()))
line_2 = set(map(lambda x :x.lower(), input().split()))
print(*sorted(line_1 | line_2))
print(*sorted(line_1 & line_2))