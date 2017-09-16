class Solution(object):
    def judgeCircle(self, moves):
        up = moves.count("U")
        down = moves.count("D")
        right = moves.count("R")
        left = moves.count("L")

        if up - down == 0:
            if right - left == 0:
                return True

        return False

print(Solution().judgeCircle("UDUDUDL"))
