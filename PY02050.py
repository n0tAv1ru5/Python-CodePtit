for _ in range(int(input())):
    ans = []
    n = int(input())
    nums_list = list(map(int, input().split()))
    for i in range(n):
        count = 1 
        j = i - 1
        while j >= 0 and nums_list[j] <= nums_list[i]:
            count += 1
            j -= 1
        ans.append(count)
    print(*ans,sep=" ")
