from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        print('store',self.store)

    #val [value, ts]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        val = self.store[key]
        l = 0
        r = len(val) -1 
        res = ""

        while(l<=r):
            mid = (l+r)//2
            if(timestamp == val[mid][1]):
                return val[mid][0]
            elif(timestamp > val[mid][1]):
                res = val[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

