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


def isValid(s: str) -> bool:
    if not check_valid(s):
        return False
    valids = {"(": ")", "{": "}", "[": "]"}
    test_s = s
    for index, c in enumerate(s):
        if c in valids.keys():
            print(c)
            last_closing_index = -1
            for index2, c2 in enumerate(s):
                if valids[c] == c2:
                    last_closing_index = index2
            print(s)
            print(last_closing_index)
            print(s[index: last_closing_index])
            
            print(last_closing_index)
# def isValid(s: str) -> bool:
#     return (
#         len(s) % 2 == 0
#         and (s.count("(") + s.count(")")) % 2 == 0
#         and (s.count("{") + s.count("}")) % 2 == 0
#         and (s.count("[") + s.count("]")) % 2 == 0
#     )


s = "(())[]{}"
result = isValid(s=s)
