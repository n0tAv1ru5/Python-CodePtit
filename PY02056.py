import math


def is_symmetry(n):
    if str(n) != str(n)[::-1] or len(str(n)) == 1:
        return False
    return True


n, _ = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = list()
max = 0
flag = 1

for idx, row in enumerate(matrix):
    for idx_item, item in enumerate(row):
        if is_symmetry(item):
            flag = 0
            if item > max:
                max = item
            ans.append((item, idx, idx_item))
if flag:
    print("NOT FOUND")
else:
    print(max)
    for loc in ans:
        if loc[0] == max:
            print("Vi tri [%d][%d]" % (loc[1], loc[2]))
