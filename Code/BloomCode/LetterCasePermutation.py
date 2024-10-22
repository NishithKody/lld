class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def util(i, val):
            if(i==n):
                res.append(val)
                return
            
            if(s[i].isalpha()):

                lw = s[i].lower()
                up = s[i].upper()

                lst1 = val + lw
                lst2 = val + up

                util(i+1, lst1)
                util(i+1, lst2)

            else:
                util(i+1, val+s[i])
        
        util(0, "")

        return res
        