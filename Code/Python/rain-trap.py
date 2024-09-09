class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left = [0] * n
        right = [0] * n
        leftMax = 0
        rightMax = 0
        res = 0

        for i in range(n):
            val = height[i]
            if(val>leftMax):
                leftMax = val
            left[i] = leftMax
        
        for i in range(n-1,-1,-1):
            val = height[i]
            if(val>rightMax):
                rightMax = val
            right[i] = rightMax

        for i in range(1,n-1):
            lm = left[i]
            rm = right[i]

            val = min(lm,rm)-height[i]
            res = res + val

        return res
       