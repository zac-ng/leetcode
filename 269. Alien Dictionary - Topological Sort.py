# https://leetcode.com/problems/alien-dictionary/
# Incomplete

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # wr -> t
        # wr -> f
        # wet and wrt

        # wrt and wrf
        # wet and wett

        # Represents the letters that can follow the key i.e. [p] = [j, k, l], j k l can follow p
        followingLetters = {}
        # Seen letters represents how many letters we have seen
        seenLetters = []
        
        prevWord = words[0]
        for word in words[1:]:
            for i in range(len(prevWord)):
                if prevWord[i] != word[i]:
                    # print(prevWord[i], word[i])
                    if prevWord[i] not in followingLetters:
                        followingLetters[prevWord[i]] = {word[i]}
                    else:
                        followingLetters[prevWord[i]].add(word[i])
                    if word[i] not in followingLetters:
                        followingLetters[word[i]] = set()
                    break
            prevWord = word

        queue = deque()
        keys = followingLetters.keys()

        for letter in keys:
            if len(followingLetters[letter]) == 0:
                queue.append(letter)
        
        output = ""
        print(followingLetters)

        while queue:
            letter = queue.popleft()
            del followingLetters[letter]
            output = letter + output
            for i in followingLetters.keys():
                if letter in followingLetters[i]:
                    followingLetters[i].remove(letter)
                if len(followingLetters[i]) == 0:
                    queue.append(i)
            print(followingLetters)         

        return output
                    
