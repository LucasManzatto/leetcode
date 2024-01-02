"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1


Steps
0 100
51 100
76 100
89 100
89 94
89 91
89 90
90
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        while left <= right:
            middle_index = (left + right) // 2
            if isBadVersion(middle_index):
                right = (
                    middle_index - 1
                )  # Narrow the search to the left half of the range
            else:
                left = (
                    middle_index + 1
                )  # Narrow the search to the right half of the range
        return left  # Return the index of the first bad version


def isBadVersion(version: int) -> bool:
    return version >= 90


n = 100
result = Solution().firstBadVersion(n)
print(result)
