class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # Brute force
        # cur_gas = 0 
        # cur_cost = 0
        # for i in range(len(gas)):
        #     ok = True
        #     tank = 0
        #     for j in range(len(gas)):
        #         index = (j + i) % len(gas)
        #         tank+= (gas[index] - cost[index])
        #         if tank < 0:
        #             ok = False
        #             break
        #     if ok:
        #         return i                
        # return -1
        n = len(gas)
        tank = 0
        res = 0
        for i in range(n):
            tank+= gas[i] - cost[i]
            if tank < 0:
                tank = 0
                res =  (i+1) % n

        return res