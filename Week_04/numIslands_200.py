class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])

        def mark(grid, i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            mark(grid, i+1, j)
            mark(grid, i, j+1)
            mark(grid, i-1, j)
            mark(grid, i, j-1)
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    cnt += 1
                    mark(grid, i, j)
        
        return cnt
