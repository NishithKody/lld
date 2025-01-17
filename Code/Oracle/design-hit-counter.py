from collections import defaultdict

class HitCounter:

    def __init__(self):
        self.hit_tracker = defaultdict(int)


    """
    @param timestamp: the timestamp
    @return: nothing
    """
    def hit(self, timestamp: int):
        self.hit_tracker[timestamp] += 1
        # print('hit_tracker',self.hit_tracker)
    """
    @param timestamp: the timestamp
    @return: the count of hits in recent 300 seconds
    """            

    def get_hits(self, timestamp: int) -> int:
        count = 0

        endtime = timestamp - 299
        if(endtime<0):
            endtime = 0
        cur = timestamp 

        while(cur>=endtime):
            if(cur in self.hit_tracker):
                count += self.hit_tracker[cur]
            cur = cur -1
        
        return count
