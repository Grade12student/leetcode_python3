class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0

        for i in range(n):
            if i > farthest:
                # If the current index is unreachable
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                # If the farthest index can reach the end
                return True
        return False
