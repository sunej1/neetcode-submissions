class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        sol = [0] * (len(digits)+1)
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + carry
            if sum < 10:
                carry = 0
            sol[i+1] = sum % 10
        if carry == 1:
            sol[0] = 1
        else:
            sol.pop(0)
        return sol

                
        