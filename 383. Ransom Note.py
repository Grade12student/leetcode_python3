class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i_count = {}
        for i in magazine:
            i_count[i] = i_count.get(i,0)+1
        for i in ransomNote:
            if i not in i_count or i_count[i] == 0:
                return False
            i_count[i]-=1
        return True