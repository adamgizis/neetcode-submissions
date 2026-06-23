class Solution:
    def isValid(self, s: str) -> bool:
        validmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c not in validmap:
                stack.append(c)
            else:
                
                if len(stack) == 0 or stack.pop(-1) != validmap[c]:
                    return False
        return len(stack) == 0
            