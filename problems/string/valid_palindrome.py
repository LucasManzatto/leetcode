"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = ""
        for char in s.lower():
            if char.isalnum():
                alpha_s += char
        return alpha_s == alpha_s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        alpha_s = ""
        for char in s.lower():
            if char.isalnum():
                alpha_s += char
        if not alpha_s:
            return True
        left = 0
        right = len(alpha_s) - 1
        while left < right:
            if alpha_s[left] != alpha_s[right]:
                return False
            left += 1
            right -= 1
        return True


s = "aa"
print(Solution().isPalindrome2(s=s))

