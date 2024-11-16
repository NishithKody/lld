from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        sorted_list = SortedList()
        n = len(nums)
        res = [0] * n

        for i in range(n-1,-1,-1):
            val = nums[i]

            if(len(sorted_list) == 0):
                sorted_list.add(val)
                res[i] = 0
                continue
            ind = sorted_list.bisect_left(val)
            res[i] = ind
            sorted_list.add(val)
        
        return res
            
        