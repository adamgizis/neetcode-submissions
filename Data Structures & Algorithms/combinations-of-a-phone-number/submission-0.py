class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        m = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"],
        }
        cur = ""
        result = []

        def dfs(index, cur):
            if index >= len(digits):
                result.append(cur)
                return
            digit = int(digits[index])
            for val in m[digit]:
                dfs(index + 1, cur + val)
            
        dfs(0, "")
        
        return result
