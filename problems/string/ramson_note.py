"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

from collections import defaultdict, Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_map = {}
        magazine_map = {}
        for c in ransomNote:
            note_map[c] = note_map.get(c, 0) + 1

        for c in magazine:
            magazine_map[c] = magazine_map.get(c, 0) + 1

        for c, total_ransom in note_map.items():
            total_maganize = magazine_map.get(c, 0)
            if total_ransom > total_maganize:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        note_map = defaultdict(int)
        magazine_map = defaultdict(int)
        for c in ransomNote:
            note_map[c] += 1

        for c in magazine:
            magazine_map[c] += 1

        for c, total_ransom in note_map.items():
            total_maganize = magazine_map[c]
            if total_ransom > total_maganize:
                return False
        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        note_map = Counter(ransomNote)
        magazine_map = Counter(magazine)

        for c, total_ransom in note_map.items():
            total_maganize = magazine_map[c]
            if total_ransom > total_maganize:
                return False
        return True

    def canConstruct4(self, ransomNote: str, magazine: str) -> bool:
        note_map = Counter(ransomNote)
        magazine_map = Counter(magazine)

        return note_map & magazine_map == note_map


ransomNote = "aa"
magazine = "aab"

result = Solution().canConstruct3(ransomNote=ransomNote, magazine=magazine)
print(result)
