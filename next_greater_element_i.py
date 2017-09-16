class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        results = []
        length = len(nums)
        for num in findNums:
            index = nums.index(num)

            found = False

            for i in range(index + 1, length):
                if nums[i] > num:
                    results.append(nums[i])
                    found = True
                    break

            if not found:
                results.append(-1)

        return results

print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
