class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        symbols = {"+", "-", "*", "/"}
        
        for num in tokens:
            print(s)
            if num in symbols:
                n2 = s.pop()
                n1 = s.pop()
                
                res = 0

                if num == "+":
                    res = n1 + n2
                elif num == "-":
                    res = n1 - n2
                elif num == "*":
                    res = n1 * n2
                else:
                    res = int(n1/n2)
                    
                s.append(res)

            else:
                s.append(int(num))

        
        return s.pop()