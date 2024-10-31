class Sea:
    def hasShip(topRight, bottomLeft):
        pass

class Point:
    def __init__(x,y) -> None:
        self.x = x
        self.y = y

class Solution:
    def shipInRect(self, sea, topRight, bottomLeft):

        def findShips(topRight, bottomLeft):
            if(topRight.x < bottomLeft.x or topRight.y < bottomLeft.y):
                return 0 
            elif(topRight.x == bottomLeft.x and topRight.y == bottomLeft.y):
                if(Sea.hasShip(topRight, bottomLeft) == True):
                    return 1
                else:
                    return 0

            if(not Sea.hasShip(topRight, bottomLeft)):
                return 0
                        
            midX = (topRight.x + bottomLeft.x)//2
            midY = (topRight.y + bottomLeft.y)//2

            topR = findShips(topRight, Point(midX+1, midY+1))
            topL = findShips(Point(midX, topRight.y), Point(bottomLeft.x, midY+1))
            botR = findShips(Point(topRight.x, midY), Point(midX, bottomLeft.y) )
            botL = findShips(Point(midX,midY), bottomLeft)
           

            return topR + topL + botL + botR
            



        res = findShips()
        return res