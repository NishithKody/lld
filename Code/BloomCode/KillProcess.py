from typing import (
    List,
)
#https://www.lintcode.com/problem/872/
class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
             we will sort your return value in output
    """
    def kill_process(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # Write your code here

        tre = {}
        for i, pt in enumerate(ppid):
            if(pt not in tre):
                tre[pt] = []
            tre[pt].append(pid[i])
            if(pid[i] not in tre):
                tre[pid[i]] = []
        # print('mapping',tre)

        res = []

        def util(node):
            if(node is None):
                return 
            
            res.append(node)
            for ngh in tre[node]:
                util(ngh)
        util(kill)
        return res

