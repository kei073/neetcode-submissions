from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        
        for s in strs:
            dd["".join(sorted(s))].append(s)

        return [val for val in dd.values()]