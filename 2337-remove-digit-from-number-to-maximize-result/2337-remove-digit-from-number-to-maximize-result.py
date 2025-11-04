class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        m= -1
        for i in range(len(number)):
            if number[i]== digit:
                if i<len(number)-1 and number[i] < number[i+1]:
                    return number[:i] + number[i+1:]
                else: 
                    m=i
        return number[:m] + number[m+1:]