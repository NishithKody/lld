class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if(len(s)==0):
            return ""

        stk = []
        stk.append(s[0])
        i = 1

        while(i<len(s)):
            val = s[i]
            
            if(len(stk)>0 and val==stk[-1]):
                if(len(stk)<(k-1)):
                    stk.append(val)
                    i = i+1
                    continue

                cnt = k-1
                chk = True

                for j in range(len(stk)-1, len(stk)-k,-1):
                    if(stk[j]!=val):
                        chk = False
                
                if(chk == True):
                    cnt = k -1
                    while(cnt>0):
                        cnt = cnt-1
                        stk.pop()
                else:
                    stk.append(val)  
            else:
                stk.append(val)
            i = i+1
        
        return "".join(stk)


#Consider counts!
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stk = []

        for i,val in enumerate(s):
            if(len(stk)==0):
                stk.append([val,1])
            else:
                [prevVal,prevCount] = stk[-1]
                if(prevVal == val):
                    prevCount = int(prevCount) + 1
                    if(prevCount == k):
                        stk.pop()
                    else:
                        stk[-1][1] += 1
                else:
                    stk.append([val,1])
     
        res = ""

        for [val,cnt] in stk:
            res = res + (val * int(cnt))
        
        return res
        