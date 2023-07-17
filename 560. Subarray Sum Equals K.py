class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        sum_map = {0: 1}  # Dictionary to store cumulative sums and their frequencies
        for i in nums:
            curr_sum += i
            complement = curr_sum - k
            if complement in sum_map:
                count += sum_map[complement]
            sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
        return count
