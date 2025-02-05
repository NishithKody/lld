class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        if(p[0]=='*' and p[1:] in s):
            return True
        
        if(p[-1]=='*' and p[:-1] in s):
            return True
        
        firstHalf, secondHalf = p.split('*')
        leftSide = s.find(firstHalf) 
        rightSide = s.rfind(secondHalf) 

        # print('left',leftSide)
        # print('right',rightSide)
        if(leftSide == -1 or rightSide == -1):
            return False
        
        if(leftSide+len(firstHalf)<=rightSide):
            return True
        else:
            return False
