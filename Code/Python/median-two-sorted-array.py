class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if(len(nums1)>len(nums2)):
            nums1,nums2 = nums2,nums1
        
        n = len(nums1) #[1,3,4,6]      1 ,3  4,6
        m = len(nums2) #[2,2,3,8]      2,4   7,8
        total = n+m

        l = 0
        r = n

        while(l<=r):
            partition1 = (l+r)//2
            partition2 = (total+1)//2 - partition1

            maxleft1 = nums1[partition1-1] if partition1 >0 else -math.inf
            minright1 = nums1[partition1] if partition1<n else math.inf

            maxleft2 = nums2[partition2-1] if partition2 >0 else -math.inf
            minright2 = nums2[partition2] if partition2<m else math.inf

            if(maxleft1<=minright2 and maxleft2<=minright1):
                if(total%2==0):
                    return (max(maxleft1,maxleft2) + min(minright1,minright2))/2
                else:
                    return max(maxleft1,maxleft2)
            elif(maxleft1>minright2):
                r = partition1 -1
            else:
                l = partition1 + 1
