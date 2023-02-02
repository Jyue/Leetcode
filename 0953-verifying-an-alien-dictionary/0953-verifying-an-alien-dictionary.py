class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        
        for word1, word2 in zip(words[:n-1],words[1:]):
   
            word1len = len(word1)
            word2len = len(word2)
        
            if word1[:word2len] == word2 and word1len > word2len:
                return False
            
   
            i = 0
            while i < min(word1len, word2len):
                # print(i, word1[i], word2[i])
                if order.index(word1[i]) > order.index(word2[i]):
                    return False
                elif order.index(word1[i]) < order.index(word2[i]):
                    break
                i += 1
            
        
        return True