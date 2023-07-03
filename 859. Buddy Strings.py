class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            # Check if there are at least two repeated characters in s
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False

        pairs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                pairs.append((s[i], goal[i]))
            if len(pairs) > 2:
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
