class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # Normalize k to be within the length of the array
        nums[:] = nums[-k:] + nums[:-k]
