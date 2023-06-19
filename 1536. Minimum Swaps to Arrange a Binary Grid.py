class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Count the number of trailing zeros in each row
        trailing_zeros = [0] * n
        for i in range(n):
            count = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros[i] = count
        
        swaps = 0
        # For each row, find the first row with enough trailing zeros
        for i in range(n):
            required_zeros = n - i - 1
            j = i
            while j < n and trailing_zeros[j] < required_zeros:
                j += 1
            if j == n:
                return -1
            # Swap rows
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                j -= 1
                swaps += 1
        return swaps
