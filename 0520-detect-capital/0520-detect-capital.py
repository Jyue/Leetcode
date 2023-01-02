class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
#       Case 1        :   USA
#       Case 2        :   leetcode
#       Case 3        :   Google

#       Check first two letters to decide which flag it belongs
#       Edge case: len(word) == 1

        if len(word) == 1: return True
    
        first_letter = word[0]
        second_letter = word[1]
        
        if first_letter.isupper() and second_letter.isupper():
            return word[2:].isupper() or len(word) == 2
        elif first_letter.islower() and second_letter.islower():
            return word[2:].islower() or len(word) == 2
        elif first_letter.isupper() and second_letter.islower():
            return word[2:].islower() or len(word) == 2
        else:
            return False