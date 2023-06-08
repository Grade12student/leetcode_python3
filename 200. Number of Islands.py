class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            grid[i][j] = "0"  # Mark the current land cell as visited
            dfs(i+1, j)      # Explore the neighboring cells in all four directions
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)  # Perform DFS to explore the island
                    res += 1   # Increment the island count
        return res
