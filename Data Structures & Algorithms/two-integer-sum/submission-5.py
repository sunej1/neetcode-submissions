class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            search = target - nums[i]
            if search in nums[i+1:]:
                return [i, i+nums[i+1:].index(search)+1]
        return [30, 30]
            