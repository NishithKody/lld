#note
# Python's heapq compares tuples element-wise.

#     First, it compares -val (frequency).
#     If frequencies are equal, it compares key (the word) in ascending lexicographical order.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = defaultdict(int)

        for word in words:
            cnt[word] += 1
        
        heap = []

        for [key,val] in cnt.items():
            heapq.heappush(heap, (-val, key))

        res = []
        for i in range(k):
            val = heapq.heappop(heap)[1]
            res.append(val)

        return res

