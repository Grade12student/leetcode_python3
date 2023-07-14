class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 0
        for i in arr:
            if i - difference in dp:
                dp[i] = dp[i - difference] + 1
            else:
                dp[i] = 1
            max_length = max(max_length, dp[i])
        return max_length