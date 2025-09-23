class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vow = ('a', 'e', 'i', 'o', 'u')
        res =[]
        prefix= []
        count=0
        for word in words:
            if word.startswith(vow) and word.endswith(vow):
                count += 1
            prefix.append(count)

        for query in queries:
            l, r = query
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] - prefix[l - 1])

        return res
