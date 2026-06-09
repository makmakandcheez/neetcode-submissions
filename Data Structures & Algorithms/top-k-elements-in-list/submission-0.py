class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        highest_counts = {}
        freq = [[] for i in range(len(nums)+1)]
        for count, num in enumerate(nums):
            for i in range(count, -1, -1):
                if i == 0:
                    freq[1].append(num)
                if num in freq[i]:
                    freq[i].remove(num)
                    freq[i+1].append(num)
                    break

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
                
        
                    
            