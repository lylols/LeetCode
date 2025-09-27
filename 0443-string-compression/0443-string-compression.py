class Solution:
    def compress(self, chars: List[str]) -> int:
        i,idx=0,0
        n= len(chars)

        while i<n:
            curr= chars[i]
            cnt=0
            while i<n and curr== chars[i]:
                i+=1
                cnt+=1
            chars[idx]= curr
            idx+=1
            if cnt>1:
                cnt= str(cnt)
                for ch in cnt:
                    chars[idx]= ch
                    idx+=1
        return idx
