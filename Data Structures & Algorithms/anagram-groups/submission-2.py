from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        
        for s in strs:
            sortedS = ''.join(sorted(s))
            dd[sortedS].append(s)

        return list(dd.values())