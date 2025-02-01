class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = triplets[0]

        for triplet in triplets[1:]:
            if(triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]):
                continue
            
            res[0] = max(res[0], triplet[0])
            res[1] = max(res[1], triplet[1])
            res[2] = max(res[2], triplet[2])

            # print('res',res)
        if(res[0]!=target[0] or res[1]!=target[1] or res[2]!=target[2]):
            return False
        
        return True
    