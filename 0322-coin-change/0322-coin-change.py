class Solution(object):
    def coinChange(self,coins, amount):
        dp = [0] + [float('inf')] * amount
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        


        