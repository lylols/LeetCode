class Solution:
    def totalMoney(self, n: int) -> int:
        summ= 0
        m = n//7
        summ+= 28*m 
        i =1
        while i<m:
            summ+= i*7
            i+=1    
        r= n%7
        summ+= ((r*(r+1))//2) +m*r
        return summ
