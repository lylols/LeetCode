class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        binary = ""
        
        while n > 0:
            rem = n % 2
            
            if rem == 0:
                binary = "1" + binary
            else:
                binary = "0" + binary
            
            n = n // 2
        
        deci = int(binary, 2)
        return deci