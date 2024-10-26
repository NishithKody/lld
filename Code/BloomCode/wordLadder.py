import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        steps= 1
        st = set(wordList)

        if(endWord not in st):
            return 0

        q = deque()
        q.append(beginWord)

        while(len(q)>0):
            l = len(q)
            for k in range(l):
                cur = q.popleft()

                if(cur == endWord):
                    return steps

                orgWord = list(cur)            
                for i,val in enumerate(orgWord):
                    ch = val
                    for letter in string.ascii_lowercase:
                        orgWord[i] = letter
                        tmp = ''.join(orgWord)
                        
                        if(tmp in st):
                            q.append(tmp)
                            st.remove(tmp)
                    orgWord[i]=ch

            steps = steps + 1

        return 0



        