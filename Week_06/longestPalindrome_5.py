class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s == 1: return s
        dp = [[0 for _ in range(len_s)] for _ in range(len_s)]

        start = 0
        max_length = 0

        for j in range(1, len_s):
            for i in range(j+1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                
                if dp[i][j] == 1:
                    cur_len = j - i + 1
                    if cur_len > max_length:
                        max_length = cur_len
                        start = i
        return s[start:start+max_length]


