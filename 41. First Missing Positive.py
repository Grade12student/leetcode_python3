class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Mark non-positive numbers as 'n+1'
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # Step 2: Mark visited indices as negative
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Step 3: Find the first positive index
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # Step 4: All indices are visited, return 'n+1'
        return n + 1