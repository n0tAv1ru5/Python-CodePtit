def count_zeros(num):
    count = 0
    while num:
        if num & 1 == 0:
            count += 1
        num >>= 1
    return count

for _ in range(int(input())):
    n, k = map(int, input().split())
    count = 0
    for i in range(n + 1):
        print(bin(i), count_zeros(i) )
           
        
    print(count)
