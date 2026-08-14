class Solution:
    def isHappy(self, n: int) -> bool:
        def addSum(m: int) -> int:
            count = (m % 10) ** 2
            while m / 10 >= 1:
                m = m//10
                count += (m % 10)**2
            return count
            
        slow = addSum(n)
        fast = addSum(slow)
        while slow != 1 and fast != 1:
            print(fast)
            slow = addSum(slow)
            fast = addSum(fast)
            if slow == fast:
                return False
            fast = addSum(fast)
            if slow == fast:
                return False
        return True
