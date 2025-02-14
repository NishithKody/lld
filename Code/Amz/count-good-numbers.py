class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod = (10**9 + 7)
        count = 0
        evenInd = (n+1)//2
        oddInd = n//2

        oddCount = pow(4, oddInd, mod)
        evenCount = pow(5, evenInd, mod)

        return (oddCount * evenCount) % mod
