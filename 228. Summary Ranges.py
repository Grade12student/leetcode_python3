class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        result = []
        start = nums[0]
        for i in range(1, n):
            if nums[i] != nums[i-1] + 1:
                if start != nums[i-1]:
                    result.append(str(start) + "->" + str(nums[i-1]))
                else:
                    result.append(str(start))
                start = nums[i]
        
        # Handle the last range
        if start != nums[n-1]:
            result.append(str(start) + "->" + str(nums[n-1]))
        else:
            result.append(str(start))
        return result
