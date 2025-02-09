class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(i,j):
            # print('swap i,j',i,j)
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        left = 0
        right = n-1
        index = 0

        while(index<=right):
            if(nums[index]==0):
                swap(index, left)
                index = index + 1
                left = left + 1
            elif(nums[index] == 2):
                swap(index, right)
                right = right -1
            else:
                index = index + 1
            # print('end of itr',nums)
        return nums
