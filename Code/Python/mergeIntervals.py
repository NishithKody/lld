class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        left = []
        right = []
        res = []
        
        for i in range(len(intervals)):
            curInt = intervals[i]

            if(curInt[0]>ni[1]):
                right.append(curInt)
            elif(curInt[1]<ni[0]):
                left.append(curInt)
            else:
                start = min(curInt[0],ni[0])
                end = max(curInt[1],ni[1])
                ni = [start,end]

        left.append(ni)
        val = left  + right
        return val
