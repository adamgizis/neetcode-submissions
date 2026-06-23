class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        st = {'+', '-', '*','/'}
        for i in tokens:
            if i in st:
                v = s.pop(-1)
                t = s.pop(-1)
                result = 0
                if i == "+":
                    result = v+t
                if i == "*":
                    result = v * t
                if i == "-":
                    result = t-v
                if i == "/":
                    result = int(t/v)
                s.append(result)
            else:
                s.append(int(i))
        
        return s[-1]
