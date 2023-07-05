from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            sort_i = "".join(sorted(i))
            ans[sort_i].append(i)
        return list(ans.values())