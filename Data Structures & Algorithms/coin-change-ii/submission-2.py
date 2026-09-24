class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        val = {}
        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            res = 0
            if a >= coins[i]:
                if (i+1, a) in val:
                    res = dfs(i+1,a)
                else:   
                    res = dfs(i + 1, a)
                if (i, a - coins[i]) in val:
                    res+=val[(i,a-coins[i])]
                else:
                    res += dfs(i, a - coins[i])
            val[(i,a)] = res
            return res
        return dfs(0, amount)







