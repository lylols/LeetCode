class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cnt=0
        for i in range(len(strs[0])):
            j=1
            while  j< len(strs) and i<len(strs[j]) and strs[0][i]==strs[j][i]:
                #cnt+=1
                j+=1
            if j== len(strs): cnt+=1
            else: break
        return strs[0][:cnt]