class Node:
    def __init__(self,val=0):
        self.val = 0
        self.children = {}
        self.ending = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if(w not in cur.children.keys()):
                nd = Node()
                cur.children[w] = nd
            cur = cur.children[w]
        cur.ending = True

    def search(self, word: str) -> bool:
        cur = self.root

        def util(cur, word):
            
            for i,w in enumerate(word):
                if(w == '.'):
                    for child in cur.children.values():
                        resUt = util(child, word[i+1:])
                        if(resUt == True):
                            return True
                    return False
                else:
                    if(w not in cur.children.keys()):
                        return False
                    cur = cur.children[w]
            return cur.ending
            
        res = util(cur,word)
        return res
