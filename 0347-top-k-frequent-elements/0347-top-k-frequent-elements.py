class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
		
        out = []
        for num, freq in counter.most_common(k):
            out.append(num)
            
        return out