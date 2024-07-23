class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        res = [False]*n
        res[len(res)-1] = True

        for i in range(n-2,-1,-1):
            val = nums[i]

            for j in range(i, i+val+1):
                if(res[j]==True):
                    res[i]=True
                    break
        return res[0]