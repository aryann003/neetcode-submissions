class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        result = []
        for s in strs:
            r = ''.join(sorted(s))
            if r not in mp:
                mp[r] = []
            mp[r].append(s)
        
        for key,values in mp.items():
            result.append(values)

        return result