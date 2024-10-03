class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        res = 0
        n = len(costs)

        def util(i,l,r):
            if(l==n/2 and r == n/2):
                return 0
            
            if(i>=n):
                return float(inf)
            
            selA = util(i+1,l+1,r) + costs[i][0]
            selB = util(i+1, l, r+1) + costs[i][1]

            return min(selA, selB)
        
        res = util(0,0,0)
        return res
            
            
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        res = 0
        n = len(costs)
        map = {}

        def util(i,l,r):
            
            if((i,l,r) in map):
                return map[(i,l,r)]

            if(l==n/2 and r == n/2):
                return 0
            
            if(i>=n):
                return float(inf)
            
            selA = util(i+1,l+1,r) + costs[i][0]
            selB = util(i+1, l, r+1) + costs[i][1]
            val = min(selA, selB)
            map[(i,l,r)] = val
            return val
        
        res = util(0,0,0)
        return res