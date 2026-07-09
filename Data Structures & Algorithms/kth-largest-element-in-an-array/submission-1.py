import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(k):
            heapq.heappush(arr, nums[i])
        for i in range(k, len(nums)):
            if arr[0] < nums[i]:
                heapq.heappush(arr, nums[i])
                heapq.heappop(arr)
        
        return arr[0]