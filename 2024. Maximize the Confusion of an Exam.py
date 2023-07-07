class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = 0
        count_T = 0
        count_F = 0
        ans = 0
        for right in range(n):
            if answerKey[right] == 'T':
                count_T += 1
            else:
                count_F += 1
            while min(count_T, count_F) > k:
                if answerKey[left] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
