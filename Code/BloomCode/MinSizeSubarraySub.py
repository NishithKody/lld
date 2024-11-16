class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = math.inf
        l = 0
        val = 0
        found = False

        for r in range(len(nums)):
            rval = nums[r]
            val = val + rval

            while(val>=target):
                res = min(res, (r-l+1))
                found = True
                lval = nums[l]
                val = val -lval
                l = l +1

        return res if found else 0