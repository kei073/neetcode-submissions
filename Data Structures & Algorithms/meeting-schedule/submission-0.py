"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        max_end = 0
        for interval in intervals:
            if max_end > interval.start:
                return False
            max_end = max(max_end, interval.end)
        
        return True