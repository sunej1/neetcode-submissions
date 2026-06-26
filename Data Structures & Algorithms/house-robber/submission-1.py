class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        memo = {}
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])   

        def helperMethod(i: int) -> int:
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(helperMethod(i-2)+nums[i], helperMethod(i-1))
            return memo[i]

        return helperMethod(len(nums)-1)
        