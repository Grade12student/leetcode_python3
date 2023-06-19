class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        current_alt = 0
        
        for g in gain:
            current_alt += g
            max_alt = max(max_alt, current_alt)
        
        return max_alt
