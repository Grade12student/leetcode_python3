class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading and trailing whitespaces
        s = s.strip()

        # Find the last space in the string
        last_space_index = s.rfind(' ')

        if last_space_index == -1:
            # No space found, the whole string is the last word
            return len(s)
        else:
            # Extract the last word using slicing
            last_word = s[last_space_index + 1:]
            return len(last_word)