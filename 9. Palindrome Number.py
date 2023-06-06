class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        reversed_str_x = str_x[::-1]
        return str_x == reversed_str_x