class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        rooms = 0

        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])

        meetings = len(intervals)

        start = 0
        end = 0

        while start < meetings:
            print(start_timings[start], "-->", end_timings[end], ":", [start, end])
            if start_timings[start] >= end_timings[end]:
                rooms -= 1
                end += 1 

            start += 1
            rooms += 1

        return rooms