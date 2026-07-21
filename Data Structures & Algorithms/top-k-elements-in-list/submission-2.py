class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num]= res.get(num, 0) + 1
        
        # create Bucket to store the numder in the idexes of their  frequecy
        # creating len(nums)+1 buckets as frequcy cannot be more than the len(nums)
        # and frequency starts from 1 so we added +1 to the len(nums)
        bucket = [[] for i in range(len(nums)+1)]

        # Fill the buckets with indexes as their frequencies
        for num, freq in res.items():
            bucket[freq].append(num)

        # Now return the K no of most frequent element
        # we can traverse reverse in list as the most frequent 
        # numbers appear at the end (index is incremental)
        # create a list to store the output and validate it's len with k
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans












