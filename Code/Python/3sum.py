class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue

            left = i+1
            right = n-1

            while(left<right):
                val = nums[i] + nums[left] + nums[right]

                if(val == 0):
                    res.append([nums[i],nums[left],nums[right]])
                    left = left +1
                    while(nums[left]==nums[left-1] and left<right):
                        left = left + 1

                elif(val>0):
                    right = right - 1
                else:
                    left = left +1
        return res
                
        