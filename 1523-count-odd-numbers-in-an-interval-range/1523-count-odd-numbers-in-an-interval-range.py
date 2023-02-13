class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        if length % 2 == 1 and low % 2 == 1:
            return length // 2 + 1

        else:
            return length // 2