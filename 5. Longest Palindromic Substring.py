class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ans = ""
        for i in range(len(s) - 1):
            # Check for odd-length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            curr_palindrome = s[l+1:r]
            ans = max(ans, curr_palindrome, key=len)
            # Check for even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            curr_palindrome = s[l+1:r]
            ans = max(ans, curr_palindrome, key=len)
        return ans
