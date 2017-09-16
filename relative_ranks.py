class Solution(object):
    def findRelativeRanks(self, nums):

        sorted_nums = list(nums)
        sorted_nums.sort(reverse=True)
        nums_and_ranks = dict()

        current_rank = 1

        for num in sorted_nums:
            if current_rank == 1:
                nums_and_ranks[num] = "Gold Medal"
            elif current_rank == 2:
                nums_and_ranks[num] = "Silver Medal"
            elif current_rank == 3:
                nums_and_ranks[num] = "Bronze Medal"
            else:
                nums_and_ranks[num] = current_rank

            current_rank += 1

        result = list()

        for num in nums:
            result.append(str(nums_and_ranks.get(num)))

        return result

print(Solution().findRelativeRanks([4, 5, 3, 2, 1]))
