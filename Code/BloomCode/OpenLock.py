class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if("0000" in deadends):
            return -1
        
        q = deque()
        visit = set(deadends)
        steps = 0

        q.append("0000")

        def getChildren(node):
            res = []

            for i in range(0,4):
                val = str((int(node[i]) + 1) % 10)
                tmp = node[:i] + val + node[i+1:]
                res.append(tmp)

                val = str(((int(node[i]) - 1)+10) % 10)
                tmp = node[:i] + val + node[i+1:]
                res.append(tmp)

            return res

        while(len(q)>0):

            for _ in range(len(q)):
                cur = q.popleft()
                if(cur == target):
                    return steps

                for child in getChildren(cur):
                    if(child in visit):
                        continue
                    
                    visit.add(child)
                    q.append(child)
            steps += 1

        return -1
