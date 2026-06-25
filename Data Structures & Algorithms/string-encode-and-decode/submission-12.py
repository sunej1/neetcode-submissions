class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output
                


    def decode(self, s: str) -> List[str]:
        output = []
        while len(s) > 0:
            count = 0
            if s[0] == "0":
                rep = 0
                s = s[2:]
            else:
                while count < len(s) and s[count].isdigit():
                    count+=1
                rep = int(s[:count])
                s = s[count+1:]

            temp = ""
            for i in range(rep):
                temp += s[0]
                s = s[1:]
            
            output.append(temp)
        return output


