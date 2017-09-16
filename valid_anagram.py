from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        if Counter(s) == Counter(t):
            return True
        else:
            return False

print(Solution().isAnagram("abs", "bsa"))

