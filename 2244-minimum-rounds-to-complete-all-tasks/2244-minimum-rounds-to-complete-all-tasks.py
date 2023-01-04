class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cntr = Counter(tasks)
        rounds = 0

        for num in cntr.values():

            if num == 1:
                return -1

            if num % 3 == 0:
                rounds += num//3
            else:
                rounds += num//3 +1
        return rounds
                    
                    