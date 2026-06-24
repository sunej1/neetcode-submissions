class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        sol = []
        for i in nums:
            counts[i] = 1 if i not in counts else counts[i] + 1
        for i in range(k):
            sol.append(max(counts, key=counts.get))
            del counts[sol[i]]
        return sol