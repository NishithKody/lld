class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        prevVal = -1
        prevCount = 0
        j = 0

        for i,val in enumerate(nums):

            if(val==prevVal and prevCount>=2):
                continue
            elif(val==prevVal):
                nums[j] = val
                prevCount += 1
            elif(val!=prevVal):
                nums[j] = val
                prevCount = 1
                prevVal = val
            
            j = j + 1

        nums[:] = nums[:j]
        