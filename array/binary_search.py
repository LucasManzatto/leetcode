"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle_index = (start + end) // 2
            middle_number = nums[middle_index]
            if target < middle_number:
                end = middle_index - 1
            elif target > middle_number:
                start = middle_index + 1
            elif target == middle_number:
                return middle_index
        return -1
                


nums = [-1,0,3,5,9,12]
target = 3
print(Solution().search(nums=nums, target=target))









