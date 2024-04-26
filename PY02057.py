import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n, _ = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = list()
item_list = set()
flag = 1

for idx, row in enumerate(matrix):
    for idx_item, item in enumerate(row):
        item_list.add(item)
        ans.append((item, idx, idx_item))
else:
    gap = max(item_list) - min(item_list)
    if gap in item_list:
        print(gap)
        for loc in ans:
            if loc[0] == gap:
                print("Vi tri [%d][%d]" % (loc[1], loc[2]))
    else:
        print("NOT FOUND")
