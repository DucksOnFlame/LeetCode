from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        count = Counter(s)

        best_index = len(s)

        for key in count:
            if count.get(key) == 1:
                this_index = s.index(key)
                if this_index < best_index:
                    best_index = this_index

        if best_index == len(s):
            best_index = -1

        return best_index

print(Solution().firstUniqChar("leetcodeleetcode"))
