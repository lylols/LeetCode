class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiv, ten=0,0
        for el in bills:
            if el== 5: fiv+=1
            elif el == 10:
                if fiv: 
                    fiv-=1
                    ten +=1
                else : return False
            else: 
                if ten and fiv:
                    ten-=1
                    fiv-=1
                elif fiv>=3:
                    fiv-=3
                else: return False
        return True