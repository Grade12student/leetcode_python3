class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # Set to keep track of seen numbers
        while n != 1:
            if n in seen:
                return False  # If n is seen again, it's in an endless cycle
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))  # Calculate the sum of squares of digits
        return True