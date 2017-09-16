class Solution(object):
    def maxProduct(self, words):
        max_product = 0
        words.sort(key=len, reverse=True)
        words_length = len(words)

        for word1 in words:
            word_index = words.index(word1)
            if word_index != words_length - 1 and len(word1) * len(words[word_index + 1]) < max_product:
                break
            word1_set = set(word1)

            for word2 in words[1:]:
                if len(word1) * len(word2) < max_product:
                    break

                word2_set = set(word2)

                comparator_set = word1_set.union(word2_set)

                if len(comparator_set) == (len(word1_set) + len(word2_set)):
                    word_length = len(word1)
                    second_word_length = len(word2)
                    if word_length * second_word_length > max_product:
                        max_product = word_length * second_word_length

        return max_product


solution = Solution()
print(solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
