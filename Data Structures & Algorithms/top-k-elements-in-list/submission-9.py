class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        print(buckets)

        for num in counts:
            print(num)
            buckets[counts[num]].append(num)
            print(buckets)
        
        res = []
        print(buckets)
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
                

