class Solution(object):
    #use DP
    #change from biggest to smallest denomination doesn't work
    def coinChange(self, coins, amount):
        dp = [0] + [-1] * amount
        for x in xrange(amount):
            if dp[x] < 0:
                continue
            for coin in coins:
                if x+coin > amount:
                    continue
                
                if dp[x+coin] < 0 or dp[x] + 1 < dp[x+coin]:
                    dp[x+coin] = dp[x] + 1
        return dp[amount]