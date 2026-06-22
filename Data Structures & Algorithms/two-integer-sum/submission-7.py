class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, n in enumerate(nums):
            dic[n] = i
        for i, n in enumerate(nums):
            search = target - n
            if search in dic and dic[search] != i:
                return [i, dic[search]]
        return