class Solution:
    def sortVowels(self, s: str) -> str:
        vow = 'aeiouAEIOU'
        ins = []
        for ch in s:
            if ch in vow:
                ins.append(ch)
        ins.sort()
        res =[]
        i=0
        for ch in s:
            if ch in vow:
                res.append(ins[i])
                i+=1
            else: res.append(ch)
        return "".join(res)