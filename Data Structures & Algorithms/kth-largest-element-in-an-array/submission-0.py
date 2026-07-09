class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [0] * k
        for i in range(k):
            arr[i] = nums[i]
        smallest = min(arr)
        for i in range(k, len(nums)):
            if smallest < nums[i]:
                arr[arr.index(smallest)] = nums[i]
                smallest = min(arr)
        
        return smallest