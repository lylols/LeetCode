class Solution:
    def partitionString(self, s: str) -> int:
        freq = [0]* 26
        cnt=1
        for el in s:
            idx = ord(el) - ord('a')
            if freq[idx] >0:
                cnt+=1
                freq[:] = [0]* 26
            freq[idx]+=1
        return cnt
