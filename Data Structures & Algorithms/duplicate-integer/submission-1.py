class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        return True if len(new_nums) != len(nums) else False
            
        