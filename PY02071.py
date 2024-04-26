def gen(n, combination, sum=0):
    if sum == n:
        ans.add(tuple(sorted(combination, reverse=True)))
        return

    for i in range(n, 0, -1):
        if sum + i <= n:
            combination.append(i)
            gen(n, combination, sum + i)
            combination.pop()


for _ in range(int(input())):
    ans = set()
    n = int(input())
    gen(n, [], 0)
    print(len(ans))
    for item in sorted(ans, reverse=True):
        print(str(item).replace(",",""),end=" ")
    print()
