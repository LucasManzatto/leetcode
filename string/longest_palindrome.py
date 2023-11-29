"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s).values()
        odds = [x for x in count if x % 2 == 1]
        # Count the total characters that have a odd total and remove 1 from each one except one, because palindromes can have one odd total
        total_odds = len(odds) - 1 if odds else 0
        return len(s) - total_odds


s = "bb"
print(Solution().longestPalindrome(s=s))
