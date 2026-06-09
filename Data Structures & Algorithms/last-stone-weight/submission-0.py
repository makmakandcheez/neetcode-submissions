class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop_max(maxHeap)
            y = heapq.heappop_max(maxHeap)
            if y < x:
                heapq.heappush_max(maxHeap, x - y)
        if len(maxHeap) == 0:
            return 0
        else:
            return maxHeap[0]   

