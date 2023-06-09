class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(1, len(letters)):
            if ord(letters[i-1]) <= ord(target) and ord(letters[i]) > ord(target):
                return letters[i]
        # If no letter satisfying the condition is found, return the first letter
        return letters[0]
