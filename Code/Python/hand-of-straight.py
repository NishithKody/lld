class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        map = defaultdict(int)

        for val in hand:
            map[val] += 1

        while(len(map)>0):
            min_val = min(map.keys())

            map[min_val] = map[min_val] - 1
            if(map[min_val]==0):
                del map[min_val]

            for i in range(groupSize-1):
                next_val = min_val + 1
                if(next_val not in map.keys()):
                    return False
                
                map[next_val] = map[next_val] - 1
                if(map[next_val]==0):
                    del map[next_val]
                min_val = next_val

        
        return True
    