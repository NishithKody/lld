class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat)

        top  = 0
        bot = n -1

        while(top<=bot):
            mid = (top+bot)//2
            # print('top,bot,mid',top,bot,mid)

            if(mat[mid][0] <= target and target <= mat[mid][-1]):
                break
            elif(target<mat[mid][0]):
                bot = bot -1 
            elif(target>mat[mid][-1]):
                top = top +1
        
        row = (top+bot)//2

        l = 0
        r = len(mat[0])-1

        while(l<=r):
            mid = (l+r)//2

            if(mat[row][mid]==target):
                return True
            elif(mat[row][mid]<target):
                l = mid + 1
            else:
                r = mid -1
        
        return False
    