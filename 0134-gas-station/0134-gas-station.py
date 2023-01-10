class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        curr = 0
        start = 0
        for i in range(len(gas)):
            
            curr += gas[i] - cost [i]
            
            if curr < 0:
                start = i + 1
                curr = 0
                
            total += gas[i] - cost [i]
            
            
        return start if total >= 0 else -1