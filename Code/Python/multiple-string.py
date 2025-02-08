class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if(num1 =='0' or num2=='0'):
            return "0"

        n = len(num1)
        m = len(num2)

        res = [0] * (n+m)

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(n):
            for j in range(m):
                firstVal = int(num1[i])
                secVal = int(num2[j])
                digit = firstVal*secVal
                res[i+j] += digit
                res[i+j+1] += res[i+j]//10
                res[i+j] = res[i+j] % 10
        
        res = res[::-1]

        finalRes = [str(x) for x in res]

        return "".join(finalRes).lstrip('0')
