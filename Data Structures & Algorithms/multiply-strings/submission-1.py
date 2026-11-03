class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sol = 0
        for n2 in range(len(num2)-1, -1, -1):
            for n1 in range(len(num1)-1, -1, -1):
                sol += int(num1[n1]) * int(num2[n2]) * 10 ** ((len(num2)-n2-1) + len(num1)-n1-1)

        return str(sol)
                
