class Solution(object):
    def removeAnagrams(self, words):
        res = []
        prev = ""

        for w in words:
            sortedWord = "".join(sorted(w))

            if sortedWord != prev:
                res.append(w)
                prev = sortedWord 

        return res      