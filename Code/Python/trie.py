class Node:
    def __init__(self,val=0):
        self.val = val
        self.children = {}
        self.ending = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if(w not in cur.children.keys()):
                nd = Node(w)
                cur.children[w]=nd
            cur = cur.children[w]
        cur.ending = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if(w not in cur.children.keys()):
                return False
            cur = cur.children[w]
        return cur.ending
        

    def startsWith(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if(w not in cur.children.keys()):
                return False
            cur = cur.children[w]
        return True
        
        