class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cntr = Counter(tasks)
        rounds = 0
        if 1 in cntr.values():
            return -1
        else:
            for num in cntr.values():
                rounds += num//3 + bool(num%3)
            return rounds
                    
                    