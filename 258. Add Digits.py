class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digits = [int(i) for i in str(num)]
            num = sum(digits)
        return num
