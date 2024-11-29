class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        n  = len(candidates)
        candidates.sort()
        
        def util(i, val, tmp):

            if(tmp == target):
                res.append(val.copy())
                return

            if(i==n):
                return 

            val.append(candidates[i])
            util(i+1, val, tmp + candidates[i])

            val.pop()
            while(i+1<n and candidates[i] == candidates[i+1] ):
                i = i+1

            util(i+1, val, tmp)           
            
        util(0, [], 0)
        return res
    