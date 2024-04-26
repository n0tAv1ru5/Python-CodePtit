def count_ways(M, N):
    dp = [[0] * N for _ in range(M)]

    dp[0][0] = 1

    for i in range(M):
        for j in range(N):
            if not (i == 0 and j == 0):
                dp[i][j] = (dp[i-1][j-2] if i-1 >= 0 and j-2 >= 0 else 0) + \
                           (dp[i-2][j-1] if i-2 >= 0 and j-1 >= 0 else 0)

    return dp[M-1][N-1]

M = int(input())
N = int(input())

result = count_ways(M, N)
print( result)
