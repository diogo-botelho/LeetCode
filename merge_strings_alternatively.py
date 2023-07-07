class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        solution = ""
        counter = 0
        len1 = len(word1)
        len2 = len(word2)

        while counter < len1 and counter < len2:
            solution = solution + word1[counter] + word2[counter]
            counter += 1

        solution = solution + word1[counter:] + word2[counter:]
        return solution
