class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([value,timestamp])
        else:
            self.map[key] = [[value,timestamp]]
        # print(self.map)

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.map:
            return result
        
        # Binary Search
        n = len(self.map[key])
        # Base Case
        if n == 1:
            return self.map[key][0][0] if self.map[key][0][1] <= timestamp else ""
        
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r) //2
            if self.map[key][mid][1] == timestamp:
                return self.map[key][mid][0]
            elif self.map[key][mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return self.map[key][r][0] if r >= 0 else ""
            
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)