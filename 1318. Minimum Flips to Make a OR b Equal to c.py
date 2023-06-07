class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1  # Get the rightmost bit of a
            bit_b = b & 1  # Get the rightmost bit of b
            bit_c = c & 1  # Get the rightmost bit of c

            if bit_c == 0:  # If the rightmost bit of c is 0
                if bit_a == 1 and bit_b == 1:  # Need to flip both a and b
                    count += 2
                elif bit_a == 1 or bit_b == 1:  # Need to flip either a or b
                    count += 1
            else:  # If the rightmost bit of c is 1
                if bit_a == 0 and bit_b == 0:  # Need to flip both a and b
                    count += 1

            a >>= 1  # Right shift a by 1 bit
            b >>= 1  # Right shift b by 1 bit
            c >>= 1  # Right shift c by 1 bit

        return count