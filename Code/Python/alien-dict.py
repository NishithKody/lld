class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        unique_char = set("".join(words))

        n = len(words)

        for i in range(n-1):
            first = words[i]
            second = words[i+1]
            minlen = min(len(first), len(second))

            if(len(first)>len(second) and first[:minlen]==second[:minlen]):
                return ""
                
            for j in range(minlen):
                if(first[j]!=second[j]):
                    adj[first[j]].add(second[j])
                    break
        
        print('adj',adj)

        visit = set()
        cycle = set()
        res = []

        def dfs(node):
            if(node in cycle):
                return False

            if(node in visit):
                return True
            
            cycle.add(node)
            visit.add(node)

            for ngh in adj[node]:
                val = dfs(ngh)
                if(val == False):
                    return False
                
            cycle.remove(node)
            res.append(node)
            return True

        for node in unique_char:
            val = dfs(node)
            if(val==False):
                return ""

        res = res[::-1]
        return ''.join(res)
