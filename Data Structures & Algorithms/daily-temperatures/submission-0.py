
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i,t in enumerate(temperatures):
            while stack != [] and t > stack[-1][1]:
                index, temperature = stack.pop(-1)
                result[index] = i-index
            stack.append((i,t))
        
        return result
