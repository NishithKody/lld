class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []

        for interval in queries:
            start = interval[0]
            end = interval[1]
            count = 0
            stk = []

            for val in s[start: end+1]:
                
                if(val == '*'):
                    stk.append(val)
                else:
                    tmp = 0
                    while(stk and stk[-1]!='|'):
                        popVal = stk.pop()
                        if(popVal == '*'):
                            tmp += 1

                    if(stk and stk[-1]=='|'):
                        count+= tmp
                    stk.append('|')

            res.append(count)
        return res
    

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        nxtCandPost = {}
        prevCantPost = {}
        prefix = []
        n = len(s)
        res = []

        nxtPos = -1
        prevPos = -1
        count = 0

        for i in range(n-1,-1,-1):
            if(s[i]=='|'):
                nxtPos = i
            nxtCandPost[i] = nxtPos
        
        for i in range(n):
            if(s[i]=='|'):
                prevPos = i
            prevCantPost[i] = prevPos

            if(s[i]=='*'):
                count+=1
            prefix.append(count)
        
        for [start, end] in queries:
            startPos = nxtCandPost[start]
            endPos = prevCantPost[end]

            tmp = 0

            if(startPos!=-1 and endPos!=-1 and startPos<endPos):
                tmp = prefix[endPos] - prefix[startPos]
            res.append(tmp)
        
        return res
