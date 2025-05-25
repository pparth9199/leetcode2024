class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key]=[]
        self.map[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        if timestamp<self.map[key][0][0]:
            return ""
        
        l=0
        r=len(self.map[key])-1
        res=""
        while l<=r:
            mid= (l+r)//2
            if self.map[key][mid][0]<=timestamp:
                l=mid+1
                res = self.map[key][mid][1]  
            else:
                r=mid-1

        return res
             


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)