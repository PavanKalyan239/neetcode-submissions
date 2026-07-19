class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def _counter(s):
            counter = {}
            for string in s:
                counter[string] = counter.get(string, 0) + 1
            return counter

        if _counter(s) == _counter(t):
            return True
        else:
            return False

        
        