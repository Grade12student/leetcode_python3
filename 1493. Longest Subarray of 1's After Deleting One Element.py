class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0
        left = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
        return max_len - 1
