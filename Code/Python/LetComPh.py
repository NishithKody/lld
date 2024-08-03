class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if(len(digits)==0):
            return []

        map  = {}
        map['1'] = []
        map['2'] = ['a','b','c']
        map['3'] = ['d','e','f']
        map['4'] = ['g','h','i']
        map['5'] = ['j','k','l']
        map['6'] = ['m','n','o']
        map['7'] = ['p','q','r','s']
        map['8'] = ['t','u','v']
        map['9'] = ['w','x','y','z']
        map['0'] = []
        res = []
        n = len(digits)

        def util(i, tmp):
            
            if(i==n):
                val = tmp.copy()
                res.append(''.join(val))
                return 
            
            for w in map[digits[i]]:
                tmp.append(w)
                util(i+1, tmp)
                tmp.pop()
        
        util(0,[])
        return res
