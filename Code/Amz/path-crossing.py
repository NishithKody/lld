class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = [0,0]
        visit = set()
        visit.add(tuple(cur))
        for p in path:
            if(p=='N'):
                cur[1] += 1
            elif(p=='S'):
                cur[1] -= 1
            elif(p=='E'):
                cur[0] += 1
            else:
                cur[0] -= 1
            
            if(tuple(cur) in visit):
                return True
            else:
                visit.add(tuple(cur))

            print('cur',cur)
        return False