class UndergroundSystem:

    def __init__(self):
        self.map = {} # id, time, station
        self.travel = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.map[id] = (t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if(id in self.map.keys()):
            #print('id found')
            [prevTime, prevStation] = self.map[id]
            diff = t - prevTime
            
            if(prevStation in self.travel.keys()):
                if(stationName in self.travel[prevStation]):
                    self.travel[prevStation][stationName].append(diff)
                else:
                    self.travel[prevStation][stationName] = [diff]
            else:
                self.travel[prevStation] = {}
                self.travel[prevStation][stationName] = [diff]
        else:
            print('not checked in')

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tr = self.travel[startStation][endStation]
        total = sum(tr)
        return total/len(tr)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)