class Solution:
    def intToRoman(self, num: int) -> str:
        
        map = {}
        map[1] = 'I'
        map[4] = 'IV'
        map[5] = 'V'
        map[9] = 'IX'
        map[10] = 'X'
        map[40] = 'XL'
        map[50] = 'L'
        map[90] = 'XC'
        map[100] = 'C'
        map[400] = 'CD'
        map[500] = 'D'
        map[900] = 'CM'
        map[1000] = 'M'

        map = dict(sorted(map.items(), reverse=True))

        res = ""
        while(num>0):
            for [val,sym] in map.items():
                if(num>=val):
                    num = num - val
                    res = res+sym
                    break

        return res