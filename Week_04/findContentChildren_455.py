class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        lg, ls = len(g), len(s)
        i, j = 0, 0
        while i < lg and j < ls:
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i
