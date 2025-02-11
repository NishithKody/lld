class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        left = 0
        right = 0

        n = len(s)

        for val in s:
            if(val=='('):
                left += 1
            else:
                right += 1
            
            if(right==left):
                maxLen = max(maxLen, right*2)
            
            if(right>left):
                left=right=0
        
        left=right=0
        for val in s[::-1]:
            if(val=='('):
                left += 1
            else:
                right += 1
            
            if(right==left):
                maxLen = max(maxLen, right*2)
            
            if(left>right):
                left=right=0
        
        return  maxLen
    