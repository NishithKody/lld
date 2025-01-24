class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res= []
        n = len(s)

        def util(i,val):

            if(i>=n):
                res.append(val.copy())
                return

            for j in range(i,n):
                tmp = s[i:j+1]
                if(tmp == tmp[::-1]):
                    val.append(tmp)
                    util(j+1,val)
                    val.pop()
    

        util(0,[])
        return res
    