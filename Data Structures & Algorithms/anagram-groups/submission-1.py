class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        result = []
        for s in strs:
            r = ''.join(sorted(s))
            mp[r].append(s)
        
        for key,values in mp.items():
            result.append(values)

        return result