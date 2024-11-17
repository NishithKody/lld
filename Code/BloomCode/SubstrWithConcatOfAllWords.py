class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_length = word_length * len(words)
        res = []
        n = len(s)

        word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1
        
        for i in range(word_length):
            left = i
            sub_count = defaultdict(int)
            count = 0

            for j in range(i,n-word_length+1, word_length):
                sub_word = s[j: j + word_length]
                if(sub_word in word_count):
                    sub_count[sub_word] += 1
                    count += 1

                    #if we have more than what is needed, shrink the window
                    while(sub_count[sub_word] > word_count[sub_word]):
                        word_to_remove = s[left: left + word_length]
                        left = left + word_length
                        sub_count[word_to_remove] -= 1
                        count -= 1

                    if(count == len(words)):
                        res.append(left)
                else:
                    sub_count.clear()
                    count = 0
                    left = j + word_length
        
        return res