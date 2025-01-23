class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        
        maxDegree = 0
        for [key, val] in map.items():
            if(val>maxDegree):
                maxDegree = val
            
        print('maxDegree',maxDegree)

        l =0
        r=0

        n = len(nums)
        wind = defaultdict(int)
        res = math.inf

        while(r<n):
            rval = nums[r]
            wind[rval] = wind[rval] + 1

            if(wind[rval]==maxDegree):
                lval = nums[l]

                while(l<r and lval!=rval):

                    wind[lval] -= 1

                    l = l + 1
                    lval = nums[l]
                res = min(res, r-l+1)
            r = r + 1

        return res
    