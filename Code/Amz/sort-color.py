class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        
        res = []
        for i in [0,1,2]:
            for j in range(map[i]):
                res.append(i)

        print(res)
        nums[:]= res

        