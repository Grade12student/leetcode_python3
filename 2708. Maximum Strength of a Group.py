class Solution:
  def maxStrength(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    pos = []
    neg = []
    zero_count =0
    
    for val in nums:
      if val > 0:
        pos.append(val)
      elif val < 0:
        neg.append(val)
      else:
        zero_count += 1
        
    neg.sort()
    popped = 0
    if len(neg) % 2 == 1:
      popped = neg.pop()
    if not pos and not neg:
      return popped if zero_count == 0 else 0
    
    base = 1
    for val in pos+neg:
      base *= val
    return base
        