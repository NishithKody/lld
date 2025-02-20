class Solution:
    def numberToWords(self, num: int) -> str:
        if(num==0):
            return 'Zero'

        less_than_20 = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }
        
        tens={
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }

        res = []
        postfix = ['',' Thousand', ' Million', ' Billion']
        index = 0

        def getWord(n):
            if(n==0):
                return ""
            res = []
            
            hundred = n//100
            if(hundred):
                res.append(less_than_20[hundred]+ " Hundred")

            last2 = n % 100
            if last2:
                if(last2>=20):
                    ten, ones = last2// 10, last2 % 10
                    res.append(tens[ten*10])
                    if(ones):
                        res.append(less_than_20[ones])
                else:
                    res.append(less_than_20[last2])            

            return " ".join(res)

        while(num>0):
            lastThree = num % 1000
            tmp = getWord(lastThree) 
            if(tmp):
                res.append(tmp + postfix[index]) 
            num = num//1000
            index = index + 1
        res.reverse()
        return " ".join(res)

