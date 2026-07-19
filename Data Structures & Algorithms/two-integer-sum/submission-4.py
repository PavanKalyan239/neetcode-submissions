class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in idx_dict:
                return [idx_dict[diff], idx]
            else:
                idx_dict[num] = idx
            

        