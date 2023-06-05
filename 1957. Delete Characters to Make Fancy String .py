class Solution:
    def makeFancyString(self, s: str) -> str:
        curr, cnt = None, 0
        res = []
        for i in s:
            if i == curr:
                cnt += 1
            else:
                curr, cnt = i, 1
            if cnt < 3:
                res.append(i)
        return ''.join(res)