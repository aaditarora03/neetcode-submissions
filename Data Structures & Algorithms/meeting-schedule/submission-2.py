
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = 0
        end = 0
        intervals.sort(key=lambda x: x.start)
        for i in intervals:
            s, e = i.start, i.end
            if s < end:
                return False
            start = s
            end = e

        return True