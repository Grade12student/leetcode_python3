class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x
        left = 1
        right = x//2
        while left<=right:
            mid = (left+right)//2
            sqrt = mid*mid
            if sqrt == x:
                return mid
            elif sqrt > x:
                right = mid-1
            else:
                left = mid+1
        return right