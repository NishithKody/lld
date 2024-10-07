class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def util(i,val):

            if(i==n):
                res.append(val.copy())
                return
            
            val.append(nums[i])
            util(i+1,val)
            val.pop()
            util(i+1,val)
        
        util(0,[])

        return res

