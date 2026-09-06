class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()

        def dfs(cur,count):
            if count == n:
                result.add(cur)
                return
            
            dfs("()"+cur, count+1)
            dfs(cur +"()", count+1)
            dfs("(" + cur + ")",count+1)

            return
        
        dfs("",0)
        
        return list(result)
