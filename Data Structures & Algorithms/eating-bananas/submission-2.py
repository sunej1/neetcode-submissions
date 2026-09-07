class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        if h == len(piles):
            return k

        def checkK(h: int, k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        # binary search on 1-k
        low = 1
        high = k
        min = k
        while low < high:
            curr = (low+high)//2
            valid = checkK(h, curr)
            if valid:
                high = curr
                if min > curr:
                    min = curr
            else: 
                low = curr+1

        return min
        
        


