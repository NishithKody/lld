import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        n = len(nums)
        l=r=0

        for r in range(n):
            while(q and nums[q[-1]]<nums[r]):
                q.pop()

            q.append(r)
            
            if(l>q[0]):
                q.popleft()
            
            if( r+1 >= k):
                res.append(nums[q[0]])
                l = l +1

        return res

