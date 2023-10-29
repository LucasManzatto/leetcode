'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals = sorted(intervals)

        current = 0
        while current < len(intervals) - 1:
            current_value = intervals[current]
            next_value = intervals[current + 1]

            overlap_interval = self.overlaps(current_value, next_value)
            
            # If there is a overlap, remove the current and next value, then add the overlap value
            # Since 2 values are removed and only one added, the current index remains the same to check
            # the new overlap value with the next value
            if overlap_interval:
                intervals.remove(current_value)
                intervals.remove(next_value)
                intervals.insert(current, overlap_interval)
            else:
                current += 1
        return intervals


    def overlaps(self, current, next):
        """
        Check if two intervals overlap and return the merged interval if they do.

        Args:
            current (List[int]): The first interval represented as [start, end].
            next (List[int]): The second interval represented as [start, end].

        Returns:
            List[int] or None: The merged interval if there is an overlap, or None if there is no overlap.

        """
        if current[1] >= next[0]:
            return [current[0], max(current[1], next[1])]
        return None
    
    
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(Solution().insert(intervals=intervals, newInterval=newInterval))