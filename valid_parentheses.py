# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:


# Input: s = "(]"
# Output: false


def check_valid(s: str) -> bool:
    return (
        len(s) % 2 == 0
        and (s.count("(") + s.count(")")) % 2 == 0
        and (s.count("{") + s.count("}")) % 2 == 0
        and (s.count("[") + s.count("]")) % 2 == 0
    )


def find_closing_pair(s, opening, valids, seen):
    last_seen_index = None
    for index, closing in enumerate(s):
        if valids[opening] == closing and index not in seen:
            last_seen_index = index
    return last_seen_index


def isValid(s: str, valids) -> bool:
    if not check_valid(s):
        return False
    seen = []
    pairs = []
    for index, c in enumerate(s):
        if index in seen:
            continue
        if c in valids.keys():
            seen.append(index)
            closing_pair_index = find_closing_pair(
                s=s, opening=c, valids=valids, seen=seen
            )
            if not closing_pair_index:
                return False
            if not check_valid(s[index : closing_pair_index + 1]):
                return False
            seen.append(closing_pair_index)
    return True


s = "(())[]{}"
valids = {"(": ")", "{": "}", "[": "]"}

result = isValid(s=s, valids=valids)
