
from numpy import matrix


def LCS(s1, s2, n, m):
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (s1[i-1] == s2[j-1]):
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
    return matrix(dp)


s1 = "aabbac"
s2 = "dabab"


# aba or bab -->> 3

dp = LCS(s1, s1[::-1], len(s1), len(s2))
print(matrix(dp))

# cur_index = [-1, -1]
# cur_max = -1
# for i in range(len(s1)+1):
#     for j in range(len(s2)+1):
#         if dp[i][j] > cur_max:
#             cur_max = dp[i][j]
#             cur_index = [i, j]


# print(cur_index, cur_max)

# ans = ""
# row = 3
# col = 5
# while(row > 0 and col > 0):
#     if dp[row][col] <= 0:
#         break
#     ans += s1[row-1]
#     col -= 1
#     row -= 1
# print(ans[::-1])
