class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        res = [-1]*n

        for i in range(2* n):
            cur = nums[i%n]
            if(not stk):
                stk.append(i)
            else:
                while(stk and cur > nums[stk[-1]]):
                    res[stk.pop()] = cur

                stk.append(i%n)  
        
        return res
