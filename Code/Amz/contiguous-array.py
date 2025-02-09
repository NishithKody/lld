class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = defaultdict(int)
        n = len(nums)

        zero = one = 0
        l = 0
        res = 0

        for r in range(n):
            rval = nums[r]
            if(rval==0):
                zero+= 1
            else:
                one+= 1
            
            if(zero == one):
                res = max(res,r+1)
            
            diff = one - zero

            if(diff in map):
                cur = r - map[diff] 
                res = max(res,cur)

            if(diff not in map):
                map[diff] = r
            
        return res
            