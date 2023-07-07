class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        subsum = 0
        ans = float('inf')
        for right in range(n):
            subsum += nums[right]
            while subsum >= target:
                ans = min(ans, right - left + 1)
                subsum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0
