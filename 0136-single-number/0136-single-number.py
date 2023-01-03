class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appear_list = []
        for num in nums:
            if num not in appear_list:
                appear_list.append(num)
            else:
                appear_list.remove(num)
        return appear_list[0]