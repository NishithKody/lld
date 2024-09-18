class MedianFinder:

    def __init__(self):
        
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if(len(self.right)>0 and (num>self.right[0])):
            heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left,-1*num)
        
        if(len(self.left)> len(self.right)+1):
            val = -1* heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        if(len(self.right)> len(self.left)+1):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -1*val)

    def findMedian(self) -> float:
        if(len(self.left)> len(self.right)):
            val = -1 * self.left[0]
            return val
        elif(len(self.right)> len(self.left)):
            val = self.right[0]
            return val
        else:
            l = self.left[0]
            r = self.right[0]
            return ((-1*l)+r)/2

        