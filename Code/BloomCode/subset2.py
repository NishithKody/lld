class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def util(i,val):
            if(i==n):
                res.append(val.copy())
                return
            
            val.append(nums[i])
            util(i+1, val)
            val.pop()
            while(i+1<n and nums[i]==nums[i+1]):
                i=i+1
            util(i+1, val)

        util(0,[])
        return res