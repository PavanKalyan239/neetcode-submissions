class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(len(nums)):
            num = 1
            for e,j in enumerate(nums):
                if e == i:
                    continue
                else:
                    num *= j
            r.append(num)
        return r