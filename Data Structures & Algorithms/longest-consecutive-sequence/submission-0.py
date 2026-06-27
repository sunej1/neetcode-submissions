class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        s = set()
        for i in nums:
            s.add(i)
        for i in s:
            count = i
            temp = 1
            while count + 1 in s:
                count += 1
                temp += 1
            if temp > max:
                max = temp
        return max
        