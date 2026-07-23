class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                num *= nums[j]
            r.append(num)
        return r