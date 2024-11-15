class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        def swap(ind1, ind2):
            nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        
        for i in range(n):
            while( 1<= nums[i] <=n and nums[i] != nums[nums[i]-1]):
                swap(i, nums[i]-1)
        

        for i in range(n):
            if(i+1 != nums[i]):
                return i+1
        
        return n+1

