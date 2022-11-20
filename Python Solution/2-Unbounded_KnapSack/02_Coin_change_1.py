def Unbounded_kanpSack_Top_Down(W, wt, val, n):
    dp = [[0]*(W+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]],  dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]


def count(coins, N, Sum):
    dp = []
    s = [0 for i in range(int(Sum)+1)]
    for i in range(N+1):
        dp.append(s)

    for i in range(N+1):
        for j in range(Sum+1):
            if (i == 0):
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 1

            elif (coins[i-1] <= j):
                dp[i][j] = (dp[i][j-coins[i-1]] + dp[i-1][j])

            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][Sum]


sum = 4
N = 3
coins = [1, 2, 3]
print(count(coins, N, sum))
