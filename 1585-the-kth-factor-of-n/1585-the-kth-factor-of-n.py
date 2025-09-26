class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        #sq= int(n**(1/2))
        cnt=1
        for f in range(1,n+1):
            if n%f==0:
                if cnt==k:
                    return f
                cnt+=1
        return -1