from sortedcollections import SortedList

class Leaderboard:
    def __init__(self):
        self.map = {}
        self.sortedScore = SortedList()
    
    def addScore(self, playerId, score):
        if(playerId not in self.map):
            self.map[playerId] = score
            self.sortedScore.add(score)
        else:
            prevScore = self.map[playerId]
            self.map[playerId] = score
            self.sortedScore.remove(prevScore)
            newScore = self.map[playerId]
            self.sortedScore.add(newScore)
    
    def top(self, k):
        return sum(self.sortedScore[-k:])
    
    def reset(self, playerId):
        prevScore = self.map[playerId]
        self.sortedScore.remove(prevScore)
        del self.map[playerId]


if(__name__=='__main__'):
    leaderboard =  Leaderboard()
    leaderboard.addScore(1,73);   #// leaderboard = [[1,73]];
    leaderboard.addScore(2,56);   #// leaderboard = [[1,73],[2,56]];
    leaderboard.addScore(3,39);   #// leaderboard = [[1,73],[2,56],[3,39]];
    leaderboard.addScore(4,51);   #// leaderboard = [[1,73],[2,56],[3,39],[4,51]];
    leaderboard.addScore(5,4);    #// leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
    print(leaderboard.top(1))           #// returns 73;
    leaderboard.reset(1);         #// leaderboard = [[2,56],[3,39],[4,51],[5,4]];
    leaderboard.reset(2);         #// leaderboard = [[3,39],[4,51],[5,4]];
    leaderboard.addScore(2,51);   #// leaderboard = [[2,51],[3,39],[4,51],[5,4]];
    print(leaderboard.top(3));           #// returns 141 = 51 + 51 + 39;