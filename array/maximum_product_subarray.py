'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

from typing import List


# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         second_index = 1
#         max_product = nums[0]
#         max_products = []
#         while second_index < len(nums):
#             product =  max_product * nums[second_index]
#             if product <= max_product:
#                 max_products.append(max_product)
#                 max_product = nums[second_index]
#             else:
#                 max_product = product
#             second_index += 1
#         max_products.append(max_product)
#         return max(max_products)


# nums = [-2,3,-4]
# print(Solution().maxProduct(nums=nums))
