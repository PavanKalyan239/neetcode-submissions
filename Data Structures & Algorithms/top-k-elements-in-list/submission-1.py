class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num]= res.get(num, 0) + 1
        so = sorted(res.items(), key=lambda item: item[1], reverse=True)
        return [so[i][0] for i in range(k)]
        