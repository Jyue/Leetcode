class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            result = []

            while len(left) and len(right):
                if (left[0] < right[0]):
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))

            result = result + left if len(left) else result + right
            return result

        def mergeSort(array):
            if len(array) < 2:
                return array

            mid = len(array)//2
            leftArray = array[:mid]
            rightArray = array[mid:]

            return merge(mergeSort(leftArray), mergeSort(rightArray))
        
        return mergeSort(nums)