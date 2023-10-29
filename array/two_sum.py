# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for x_index, x in enumerate(nums):
        for y_index, y in enumerate(nums[x_index + 1 :]):
            if x + y == target:
                return sorted([x_index, y_index + x_index + 1])

# Time complexity solution
# Using a hash table to transverse the array only one time
def twoSum2(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, x in enumerate(nums):
        complement = target - x
        if complement in seen.keys():
            return [index, seen[complement]]
        seen[x] = index
    return None


nums = [2, 5, 5, 11]
target = 10
result = twoSum2(nums=nums, target=target)
