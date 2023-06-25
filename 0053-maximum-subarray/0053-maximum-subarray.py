class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=nums
        summ=0 
        maxi=arr[0]
        for i in arr:
            
            summ+=i
            if summ>maxi:
                maxi=summ
            if summ<0:
                summ=0
        return maxi