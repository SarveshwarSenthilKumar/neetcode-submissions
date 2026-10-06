"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        longestInterval = []
        for interval in intervals:
            intervalDuration = interval.end-interval.start
            for longInterval in longestInterval:
                longDuration = longInterval.end-longInterval.start
                if interval.start > longInterval.start and interval.start < longInterval.end:
                    return False
                elif interval.end > longInterval.start and interval.end < longInterval.end:
                    return False
                elif interval.start == longInterval.start and interval.end == longInterval.end:
                    return False
                elif interval.start <= longInterval.start and interval.end >= longInterval.end:
                    return False
            longestInterval.append(interval)
        return True