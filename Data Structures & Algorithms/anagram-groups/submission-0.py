class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            d,e = {}, {}
            for i in range(len(s)):
                d[s[i]] = d.get(s[i], 0) + 1
                e[t[i]] = e.get(t[i], 0) + 1
            return d == e

        res = []
        for s in strs:
            if not res:
                res.append([s])
            else:
                for item in res:
                    if isAnagram(s, item[0]):
                        item.append(s)
                        break
                else:
                    res.append([s])
        return res      
    