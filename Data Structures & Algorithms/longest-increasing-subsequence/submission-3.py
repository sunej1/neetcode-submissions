class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        memo[len(nums)-1] = 1

        def helperMethod(i: int, min: int) -> int:
            if memo[i] != -1:
                return memo[i]
            vals = set()
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    vals.add(helperMethod(j, nums[i]))
            if len(vals) == 0:
                memo[i] = 1
            else:
                memo[i] = 1+max(vals)
            return memo[i]

            
        for i in range(len(nums)):
            memo[i] = helperMethod(i, 0)
        return max(memo)
        