class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token == "+" or token == "-" or token == "/" or token == "*":
                popped1 = stack.pop()
                popped2 = stack.pop()
                if token == "+":
                    stack.append(int(popped1) + int(popped2))
                if token == "-":
                    stack.append(int(popped2) - int(popped1))
                if token == "/":
                    if int(popped2)/int(popped1) >= 0:
                        stack.append(int(popped2) // int(popped1))
                    else:
                        stack.append((-1)*((-1)*int(popped2) // int(popped1)))
                if token == "*":
                    stack.append(int(popped1) * int(popped2))
            else:
                stack.append(token)
            
        return stack[0]