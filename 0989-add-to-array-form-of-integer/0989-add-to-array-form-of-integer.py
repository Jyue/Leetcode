class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        carry = 0
        for i in range(len(num)-1, -1, -1):
            if carry:
                num[i] += carry
            carry, res = divmod(num[i], 10)
            num[i] = res
        while carry:
            num = [carry] + num
            carry, res = divmod(num[0], 10)
            num[0] = res
        return num