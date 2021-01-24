class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_p = len(prices)
        # dp = [[0, 0] for _ in range(len_p)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, len_p):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        #     dp[i][1] = max(dp[i-1][1], -prices[i])
        # return dp[-1][0]
        
        # 状态压缩
        hold, nothing = -prices[0], 0

        for p in prices:
            hold = max(hold, -p)
            nothing = max(nothing, p+hold)
        return nothing