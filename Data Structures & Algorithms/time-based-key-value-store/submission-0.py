class Node:
    def __init__(self, key, val, ts):
        self.key = key
        self.val = val
        self.ts = ts


class TimeMap:

    def __init__(self):
        self.mmap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        node = Node(key,value,timestamp)
        if key not in self.mmap:
            self.mmap[key] = []
        self.mmap[key].append(node)

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        vals = self.mmap.get(key, [])
        left = 0
        right = len(vals) - 1

        while left <= right:
            mid = (left + right) // 2
            if vals[mid].ts > timestamp:
                right = mid - 1
            else:
                result = vals[mid].val
                left = mid + 1

        return result
        
