class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        map = defaultdict(int)
        map[0] = 1
        prefix = 0

        for val in nums:
            prefix = prefix + val

            if((prefix - k) in map):
                res = res + map[prefix-k]

            map[prefix] += 1

        return res            
            