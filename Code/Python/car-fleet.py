class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        fleet = {}
        n = len(position)

        for i in range(n):
            fleet[position[i]] = speed[i]
        
        fleet = dict(sorted(fleet.items(), key=lambda x:x[0], reverse=True))

        for pos,spd in fleet.items():
            time = (target-pos)/spd
            if(len(stk)==0):
                stk.append(time)
                continue
            
            if(time<=stk[-1]):
                continue
            
            stk.append(time)

        return len(stk)
    