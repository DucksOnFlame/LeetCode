class Solution(object):
    def titleToNumber(self, s):

        col_num = 0

        for letter in s:
            col_num *= 26
            col_num += ord(letter) - int("A")

        return col_num

print(Solution().titleToNumber("AAA"))
