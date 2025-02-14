class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = n -1

        for i in range(n-2, -1, -1):
            if(nums[i]<nums[i+1]):
                index = i
                break
            
        print('index',index)
        
        for j in range(n-1, index, -1):
            if(nums[j]>nums[index]):
                print('next higher at',j)
                nums[index], nums[j] = nums[j], nums[index]
                break

        l = index + 1
        r = n -1

        while(l<r):
            nums[l],nums[r] = nums[r], nums[l]
            l=l+1
            r=r-1
        