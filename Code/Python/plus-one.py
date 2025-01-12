class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            val = digits[i] + carry
            carry = val//10
            val = val % 10
            digits[i] = val
        
        if(carry == 1):
            digits = [1] + digits
        
        return digits
        