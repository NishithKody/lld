class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        map = defaultdict(list)
        minSoFar = math.inf
        arr.sort()
        n = len(arr)

        for i in range(n-1):
            sec = arr[i+1]
            first = arr[i]

            diff = sec - first
            map[diff].append([first, sec])
            if(diff<minSoFar):
                minSoFar = diff
            
        return map[minSoFar]
