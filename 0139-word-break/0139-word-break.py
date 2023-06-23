class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # dp store a set of j that 0->j-1 can be break successfully, j = 0->n
    # time O(N^3) worst space O(N)
        if not s or not wordDict:
            return False

        word_set = set(wordDict)

        # if words only have a few length, we don't need to check substring that has other lengths, thus save  time
        length_set = set() 
        for word in wordDict:
            length_set.add(len(word))

        n = len(s)
        dp = set([0]) # store a set of j that 0->j-1 can be break successfully, j=0 means empty

        for cur in range(1, n + 1):
            for prev in dp:
                if cur - prev in length_set and s[prev: cur] in word_set:
                    dp.add(cur)
                    break

        return n in dp
        