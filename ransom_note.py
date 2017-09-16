class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        if len(ransomNote) > len(magazine):
            return False

        letter_list = list(magazine)

        for letter in ransomNote:
            if letter in letter_list:
                letter_list.pop(letter_list.index(letter))
            else:
                return False

        return True

print(Solution().canConstruct("a", "ab"))
