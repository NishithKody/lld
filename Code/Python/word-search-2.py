class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add(self, word):
        cur = self

        for w in word:
            if(w not in cur.children):
                node = TrieNode()
                cur.children[w] = node
            cur = cur.children[w]
        
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        n = len(board)
        m = len(board[0])
        res = set()
        visit = set()

        trie = TrieNode()
        for word in words:
            trie.add(word)

        def dfs(r, c, node, wd):
            if(r>=n or c>=m or r<0 or c<0 
                or (r,c) in visit
                or board[r][c] not in node.children
                ):
                return
            
            visit.add((r,c))
            wd = wd + board[r][c]
            node = node.children[board[r][c]]

            if(node.isWord):
                res.add(wd)
            
            dfs(r+1, c, node, wd )
            dfs(r-1, c, node, wd )
            dfs(r, c+1, node, wd )
            dfs(r, c-1, node, wd )
            visit.remove((r,c))
        
        for i in range(n):
            for j in range(m):
                dfs(i,j, trie, "")
        
        return list(res)
            
