class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        last_Idx = defaultdict()
        
        i = 0
        for j, Type in enumerate(fruits):
            # print(i,j,last_Idx)
            if Type not in last_Idx and len(last_Idx) >= 2:
                max_len = max(max_len, j - i)
                i = min(last_Idx.values()) + 1
                del last_Idx[min(last_Idx, key=last_Idx.get)]
            last_Idx[Type] = j
        max_len = max(max_len, j - i + 1)
        return max_len
                    