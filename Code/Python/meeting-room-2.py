"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# To solve this problem, we need to keep track of both the 
# start time and the end time
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if(len(intervals)==0):
            return 0
        intervals.sort(key=lambda x:x.start)
        heap = []
        count = 1

        heapq.heappush(heap,intervals[0].end)

        for interval in intervals[1:]:
            if(heap[0]>interval.start):
                heapq.heappush(heap,interval.end)
            else:
                val = heapq.heappop(heap)
                heapq.heappush(heap,interval.end)
            
            if(len(heap)>count):
                count = len(heap)

        
        return count
