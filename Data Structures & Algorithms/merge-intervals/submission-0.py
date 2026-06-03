class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                interval = res.pop()
                interval = [min(interval[0], intervals[i][0]), max(interval[1], intervals[i][1])]
                res.append(interval)
            else:
                res.append(intervals[i])
        
        return res