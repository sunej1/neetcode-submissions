class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        full = 0
        for i in range(len(nums)+1):
            full += i
        return full - total