class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        memo = {}

        def dfs(i):
            if i > high:
                return 0
            if i in memo:
                return memo[i]

            ans = 0
            if low <= i <= high:
                ans += 1
            ans += dfs(i + zero) + dfs(i + one)
            ans %= mod

            memo[i] = ans
            return ans

        return dfs(0)
