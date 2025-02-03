class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        map = defaultdict(int)
        tsum = 0
        for num in nums:
            map[num] += 1
            tsum += num
        
        # outlier  = tsum -(2 * special) 
        largOut = -math.inf
        for num in nums:
            val = tsum - (2 * num)
            
            if(val in map):
                if(val!=num or map[val]>=2):
                    largOut = max(largOut, val)
        
        return largOut
