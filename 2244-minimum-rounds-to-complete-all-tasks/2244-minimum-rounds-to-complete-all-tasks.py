class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cntr = Counter(tasks)
        rounds = 0
        if 1 in cntr.values():
            return -1
        else:
            for num in cntr.values():
                if num % 3 == 0:
                    rounds += num//3
                else:
                    rounds += num//3 +1
            return rounds
                    
                    