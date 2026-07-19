class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for num_1 in range(len(nums)):
            for num_2 in range(num_1 + 1, len(nums)):
                if nums[num_1] + nums[num_2] == target:
                    return [num_1, num_2]
            

        