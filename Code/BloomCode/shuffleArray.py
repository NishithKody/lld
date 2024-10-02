class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.org = nums.copy()

    def reset(self) -> List[int]:
        self.arr = self.org.copy()
        return self.arr

    def shuffle(self) -> List[int]:
        n = len(self.arr)
        res = []
        for i in range(n-1,-1,-1):
            index = random.randint(0,i)
            val = self.arr[index]
            res.append(val)

            self.arr[index],self.arr[i] = self.arr[i],self.arr[index]
        
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()