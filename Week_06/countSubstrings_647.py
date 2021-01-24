class Solution:
    def countSubstrings(self, s: str) -> int:
        len_n = len(s)
        dp = [[0 for _ in range(len_n)] for _ in range(len_n)]
        ans = 0
        for j in range(len_n):
            for i in range(j+1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1
        return ans
