class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [1] * n  # Initialize the lengths of increasing subsequences
        counts = [1] * n   # Initialize the counts of increasing subsequences
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:   # If the current element nums[i] can extend the increasing subsequence ending at nums[j]
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        max_len = max(lengths)
        ans = sum(count for length, count in zip(lengths, counts) if length == max_len)
        return ans
