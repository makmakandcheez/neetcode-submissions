class TimeMap:

    def __init__(self):
        self.stamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if not self.stamps[key]:
            return ""
        max_time = self.stamps[key][0]
        res = ""
        l, r = 0, len(self.stamps[key]) - 1

        while l <= r:
            m = l + (r - l) // 2
            if self.stamps[key][m] == timestamp:
                return self.values[key][m]
            elif timestamp > self.stamps[key][m]:
                max_time = max(max_time, self.stamps[key][m])
                res = self.values[key][self.stamps[key].index(max_time)]
                l = m + 1
            else:
                r = m - 1
        return res
                
