class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split()[::-1]
        l = []
        for i in ss:
            l.append(i)
        return " ".join(l)