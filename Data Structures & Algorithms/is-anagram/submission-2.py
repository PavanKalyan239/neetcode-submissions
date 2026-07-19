class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        _counterS, _counterT = {}, {}

        for i in range(len(s)):
            _counterS[s[i]] = _counterS.get(s[i],0) + 1
            _counterT[t[i]] = _counterT.get(t[i],0) + 1

        return _counterS == _counterT
           
        