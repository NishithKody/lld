class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda item:item[0])

        res = []
        res.append(intervals[0])


        for interval in intervals[1:]:
            cur = res[-1]
            nxt = interval

            if(cur[1] >= nxt[0]):
                start = min(cur[0], nxt[0])
                end = max(cur[1], nxt[1])
                res.pop()
                res.append([start, end])
            else:
                res.append(nxt)
        
        return res
    