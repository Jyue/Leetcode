class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            hashmap[numbers[i]] = i
        print(hashmap)
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if (complement in hashmap) and hashmap[complement] != i:
                return [i+1, hashmap[complement]+1] 