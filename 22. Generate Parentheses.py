class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # Recursive helper function to generate parentheses
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        # Start the backtrack with an empty string and 0 left and right parentheses
        backtrack('', 0, 0)
        return res
