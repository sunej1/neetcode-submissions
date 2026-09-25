class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        memo[len(nums)-1] = 0

        def helperMethod(i: int) -> int:
            if memo[i] != -1:
                return memo[i]
            for jump in range(1, nums[i]+1):
                if i+jump >= len(nums):
                    continue
                memo[i+jump] = helperMethod(i+jump)
            if (i+nums[i]+1)-(i+1) <= 0:
                memo[i] = len(nums)
            else:
                memo[i] = 1+min(memo[i+1:i+nums[i]+1])
            return memo[i]

        memo[0] = helperMethod(0)
        print(memo)
        return memo[0]

        