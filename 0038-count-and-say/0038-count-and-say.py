class Solution:
    def countAndSay(self, n: int) -> str:
        res="1"
        for i in range(1,n):
            curr= res[0]
            cnt=1
            temp=""
            for j in res[1:]:
                if j==curr: cnt+=1
                else:
                    temp+= str(cnt)+curr
                    curr =j
                    cnt=1
            res = temp + str(cnt) + curr

        return res
                
