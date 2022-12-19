# https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


# class Solution:

#     # Function to find the maximum money the thief can get.
#     def FindMaxSum(self, a, n):

#         dp = [0 for i in range(n+1)]
#         return self.solve(n, a, dp)

def solve(ind, a, dp):
    if ind == 0:
        return a[ind]
    if ind < 0:
        return 0
    if(dp[ind] != -1):
        return dp[ind]
    pick = a[ind]+solve(ind-2, a, dp)
    notpick = solve(ind-1, a, dp)
    dp[ind] = max(pick, notpick)
    return dp


n = 6

dp = [-1 for i in range(n+1)]
a = [5, 5, 10, 100, 10, 5]
# ob = Solution()
# aav = ob.FindMaxSum(a, n)
# print(aav)
print(solve(n-1, a, dp))
