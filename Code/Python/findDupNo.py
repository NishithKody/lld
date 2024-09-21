class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slw = fst = 0

        while(True):
            slw = nums[slw]
            fst = nums[nums[fst]]
            if(slw==fst):
                break
        
        print('the slw',slw)
        cur = 0
        while(cur!=slw):
            cur = nums[cur]
            slw = nums[slw]
        
        return cur
