class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        memo[len(nums)-1] = True

        def helperMethod(i: int) -> bool:
            if i in memo:
                return memo[i]
            if nums[i] == 0:
                memo[i] = False
                return False
            for j in range(1,nums[i]+1):
                if helperMethod(j+i):
                    memo[j+i] = True
                    return True
            memo[i] = False
            return False

        memo[0] = helperMethod(0)
        return memo[0]

        