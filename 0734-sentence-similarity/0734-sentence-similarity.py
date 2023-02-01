class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        
        similarPairsMap = defaultdict(list)
        
        for similarPair in similarPairs:
            similarPairsMap[similarPair[0]].append(similarPair[1])
            similarPairsMap[similarPair[1]].append(similarPair[0])
        
        for word1, word2 in zip(sentence1, sentence2) :
            if word2 not in similarPairsMap[word1] and word1!=word2:
                return False
        return True