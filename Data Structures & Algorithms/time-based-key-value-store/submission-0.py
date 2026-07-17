class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []

        self.mp[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        arr = self.mp[key]
        start = 0
        end = len(arr)-1
        ans = ""
        while start <= end:
            mid = (start+end)//2
            val , time = arr[mid]
            if time <= timestamp:
                ans = val
                start = mid+1
            else:
                end = mid-1
        return ans

        
