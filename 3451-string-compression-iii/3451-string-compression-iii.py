class Solution:
    def compressedString(self, word: str) -> str:
        curr= word[0]
        cnt=0
        ans=""
        for c in word:
            if c==curr and cnt==9:
                ans+= str(cnt)+c
                cnt=1
            elif c==curr:
                cnt+=1
            else:
                ans+= str(cnt)+curr
                curr= c
                cnt=1
        ans+=str(cnt) + curr
        return ans
                