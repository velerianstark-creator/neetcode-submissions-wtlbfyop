class TimeMap:

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            l = 0
            r = len(self.store[key]) - 1
            if self.store[key][l][0] > timestamp:
                return ""
            while l < r:
                mid = (l + r) // 2
                if self.store[key][mid][0] == timestamp:
                    return self.store[key][mid][1]
                if self.store[key][mid][0] < timestamp:
                    l = mid + 1
                elif self.store[key][mid][0] > timestamp:
                    r = mid
            if self.store[key][l][0] <= timestamp:
                return self.store[key][l][1]
            elif self.store[key][l][0] > timestamp and l > 0:
                return self.store[key][l - 1][1]
        return ""
