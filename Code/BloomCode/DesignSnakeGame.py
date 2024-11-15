from collections import deque
from  typing import List

class SnakeGame:

    def __init__(self, width: int, height: int, foods: List[List[int]]) -> int:
        self.q = deque()
        self.visit = set()
        self.q.append([0,0])
        self.visit.add((0,0))
        self.score = 0
        self.w = width
        self.h = height
        self.foods = deque(foods)

    """
    @param direction: the direction of the move
    @return: the score after the move
    """
    def move(self, direction: str) -> int:
        # write your code here
        h_r, h_c = self.q[-1]

        if(direction == 'r' ):
            h_c += 1
        elif(direction == 'l' ):
            h_c -= 1
        elif(direction == 'u' ):
            h_r -= 1
        elif(direction == 'd' ):
            h_r += 1
        
        if(h_r>=self.h or h_r<0 or h_c>=self.w or h_c<0):
            return -1

        if([h_r,h_c] in self.foods):
            self.score += 1
            self.foods.popleft()
        else:
            rem_r, rem_c = self.q.popleft()
            self.visit.remove((rem_r,rem_c))
                
        if((h_r,h_c) in self.visit):
            return -1
                
        self.q.append((h_r, h_c))
        self.visit.add((h_r, h_c))

        return self.score
            