class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  # Time: O(n*m*n) and Space: O(n)

        dp = [False] * (len(s) + 1)  # creating a dp list with one extra index
        dp[len(s)] = True            # 0-8: to store true in case of we have to check the string for empty wordDict

        for i in range(len(s) - 1, -1, -1):  # we will take 1, 2, 3, 4, .. characters at time from string
            for w in wordDict:               # and check if the words in wordDict matches with the characters
			
                # current index in string +  words length should be less than the total string length and
                # string from current index till the length of the word should with match the actual word from wordDict
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:  
				    # when it's true we will store the boolean value
                    # in dp's current index from the index in dp[current index + length of the word]
                    # this will make sure that we are not taking any matching characters from in between the string that
                    # will disturb the equivalent of the string i.e. s = |leet|code|code|r & w = leet, code, coder?
                    # that we are taking from one end of an array i.e. s = |leet|code|coder| & w = leet, code, coder
                    dp[i] = dp[i + len(w)]

                if dp[i]:  # after the current index is set to True, we cannot continue to check the rest of the words from wordDict
                    break

        return dp[0]  # if every subsequence in string in found in wordDict then index 0 will be set to True else False