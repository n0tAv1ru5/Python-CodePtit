import math

input()
a = sorted(list(map(int, input().split())))
print(max(a[0] * a[1], max(a[-1] * a[-2], max(a[0] * a[1] * a[-1], a[-1] * a[-2] * a[-3]))))

