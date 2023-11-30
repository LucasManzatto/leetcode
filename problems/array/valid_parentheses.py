class Solution:
    def check_valid(self, s: str) -> bool:
        return (
            len(s) % 2 == 0
            and (s.count("(") + s.count(")")) % 2 == 0
            and (s.count("{") + s.count("}")) % 2 == 0
            and (s.count("[") + s.count("]")) % 2 == 0
            and s.count("(") - s.count(")") == 0
            and s.count("{") - s.count("}") == 0
            and s.count("[") - s.count("]") == 0
        )

    def find_closing_pair(self, s, opening, valids, seen, start_index):
        last_seen_index = None
        for index, closing in enumerate(s):
            if index < start_index:
                continue
            if valids[opening] == closing and index not in seen:
                last_seen_index = index
        return last_seen_index

    def isValid(self, s: str) -> bool:
        valids = {"(": ")", "{": "}", "[": "]"}
        if not self.check_valid(s):
            return False
        seen = []
        pairs = []
        for index, c in enumerate(s):
            print(index, c, seen)
            if index in seen:
                continue
            if c in valids.keys():
                print(c)
                seen.append(index)
                closing_pair_index = self.find_closing_pair(
                    s=s, opening=c, valids=valids, seen=seen, start_index=index
                )
                print(index, closing_pair_index)
                print(s[index : closing_pair_index + 1])
                if not closing_pair_index:
                    return False
                if not self.check_valid(s[index : closing_pair_index + 1]):
                    return False
                seen.append(closing_pair_index)
        return True


s = "({(())}[()])"
valid = Solution().isValid(s=s)
