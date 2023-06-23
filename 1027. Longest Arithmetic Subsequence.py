from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)  # Dictionary to store the length of longest arithmetic subsequence
        max_length = 0
        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                # Check if a subsequence with the same difference already exists ending at index i
                dp[(j, diff)] = dp[(i, diff)] + 1
                # Update the maximum length
                max_length = max(max_length, dp[(j, diff)])
        return max_length + 1
