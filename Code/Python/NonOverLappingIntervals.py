#The trick is sorting by the end time, since the least end time will be the first to end, it should come in the result.
#try examples by sorting by the end time

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0
        res = []

        inters = sorted(intervals, key=lambda item:item[1])
        # print(inters)

        i = 1
        res.append(inters[0])
        while(i<len(inters)):
            cur = inters[i]
            prev = res[len(res)-1]
            
            if(prev[1]>cur[0]):
                count = count+1
                i=i+1
                continue
            else:
                res.append(cur)
                i=i+1
        
        return count

