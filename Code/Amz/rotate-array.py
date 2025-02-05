class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = [0] * n

        for i in range(n):
            val = nums[i]
            newIndex = (i+k)%n
            tmp[newIndex] = val

        nums[:] = tmp

#space optimized
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def rev(arr,l,r):

            while(l<r):
                arr[l],arr[r]=arr[r],arr[l]
                l=l+1
                r=r-1
        k=k%n
        rev(nums,0,n-1)
        rev(nums, 0, k-1)
        rev(nums, k, n-1)
            

