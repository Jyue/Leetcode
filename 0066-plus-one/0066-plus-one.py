class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = len(digits)
        carry = 1
        i = 0
        while carry and i < m:
            carry, last_digit = divmod(digits[m-1-i] + carry, 10)
            digits[m-1-i] = last_digit
            i += 1
            
        if carry and i == m:
            return [1]+digits
        else:
            return digits