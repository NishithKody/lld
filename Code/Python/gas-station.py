class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        res = 0
        if(sum(gas)<sum(cost)):
            return -1
        
        n = len(gas)
        total = 0
        for i in range(n):
            curGas = gas[i]
            curCost = cost[i]

            diff = curGas - curCost
            total = total + diff

            if(total<0):
                total = 0
                res = i + 1
        
        return res
    