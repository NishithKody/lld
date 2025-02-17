class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = [n] * n
        res[-1] = 0
       
        for i in range(n-2,-1,-1):
            val = nums[i]
            for j in range(i, i+val+1):
                if(j<n and res[j]!=n ):
                    res[i] = min(res[i], res[j]+1)
        
        return res[0] if res[0]!=n else -1
