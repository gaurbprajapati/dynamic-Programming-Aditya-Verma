
from numpy import matrix


def LCS(s1, s2, n, m):
    dp = [[0]*(m+1) for i in range(n+1)]
    cur_max = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            if (s1[i-1] == s2[j-1]):
                dp[i][j] = 1+dp[i-1][j-1]
                if (dp[i][j] > cur_max):
                    cur_max = dp[i][j]
            else:
                dp[i][j] = 0
    return cur_max


s1 = "aaa"
s2 = "dabab"


# aba or bab -->> 3

ans = LCS(s1, s1[::-1], len(s1), len(s1))

print(ans)
