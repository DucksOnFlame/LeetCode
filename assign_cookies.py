class Solution(object):
    def findContentChildren(self, g, s):
        g.sort(reverse=True)
        s.sort(reverse=True)

        max_satisfied = min(len(g), len(s))

        children = g[-max_satisfied:]
        cookies = s[:max_satisfied]

        satisfied = 0

        for cookie in cookies:
            for child in children:
                if cookie >= child:
                    children.pop(children.index(child))
                    satisfied += 1
                    break

        return satisfied


print(Solution().findContentChildren([1, 2, 3], [1, 1]))
print(Solution().findContentChildren([1, 2], [1, 2, 3]))
