class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = ""
        for i in range(len(nums)-1):
            if flag:
                if flag == "I" and nums[i] > nums[i+1]:
                    return False
                if flag == "D" and nums[i] < nums[i+1]:
                    return False
            else:
                if nums[i] < nums[i+1]:
                    flag = "I"
                if nums[i] > nums[i+1]:
                    flag = "D"
        return True
                