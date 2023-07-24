class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) #{1, 2, 3, 100, 4, 200}
        max_length = 0
        for num in num_set: # Check if the current number is the start of a sequence
            if num - 1 not in num_set:
                current_length = 1
                current_num = num + 1   # Count the length of the consecutive sequence starting from the current number
                while current_num in num_set:
                    current_length += 1
                    current_num += 1
                # Update the maximum length if necessary
                max_length = max(max_length, current_length)
        return max_length
