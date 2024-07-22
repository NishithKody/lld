class Solution:
    def findMin(self, nums: List[int]) -> int:

        if(len(nums)==1):
            return nums[0]
            
        low = 0
        high = len(nums)-1

        mid = (low+high)//2

        while(low<=high):
            mid = (low+high)//2
            if(nums[mid]>nums[mid+1]):
                return nums[mid+1]
            elif(nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]):
                return nums[mid]
            elif(nums[mid]>nums[0] and nums[mid]>nums[len(nums)-1]):
                low = mid+1
            else:
                high = high-1
        
        return nums[mid]

        