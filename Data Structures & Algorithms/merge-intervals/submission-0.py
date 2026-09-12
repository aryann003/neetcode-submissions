
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                # Overlapping intervals
                end = max(end, intervals[i][1])
            else:
                # No overlap, save current interval
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        # Add the final interval
        result.append([start, end])

        return result

