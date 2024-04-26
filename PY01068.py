from itertools import combinations

n, k = map(int, input().split())
name = sorted(set(input().split()))

combination_list= combinations(name,k)
for item in combination_list:
    print(*item)
