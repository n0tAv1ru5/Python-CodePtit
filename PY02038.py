coin_map = [list(input()) for _ in range(int(input()))]
count = 0

for row in coin_map:
    n = row.count("C")
    count += (n * (n - 1)) // 2
for column in zip(*coin_map):
    n = column.count("C")
    count += (n * (n - 1)) // 2
    
print(count) 