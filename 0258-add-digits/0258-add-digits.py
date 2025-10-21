class Solution:
    def addDigits(self, num: int) -> int:
        el=num
        while el//10!=0:
            summ=0
            while(el):
                summ+= el%10
                el//= 10
            el=summ
        return el
