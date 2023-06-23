class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = [0] * 26
        t_counts = [0] * 26
        for char in s:
            s_counts[ord(char) - ord('a')] += 1
        for char in t:
            t_counts[ord(char) - ord('a')] += 1
        return s_counts == t_counts
