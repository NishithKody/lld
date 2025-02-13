from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        # Write your code here
        intervals = []
        res = []
        for sch in schedule:
            for i in range(0,len(sch),2):
                fr = sch[i]
                sc = sch[i+1]

                intervals.append([fr,sc])
        
        intervals.sort(key=lambda item:item[0])

        prevEnd = -math.inf

        for interval in intervals:
            curStr, curEnd = interval[0], interval[1]

            if(curStr<=prevEnd):
                prevEnd = max(prevEnd, curEnd)
            else:
                intr = Interval(prevEnd, curStr)
                res.append(intr)
                prevEnd = curEnd
        
        return res[1:]
