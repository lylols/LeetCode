class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = False
        cnt =0
        words =1
        for ch in text:
            if ch in brokenLetters:
                broken = True
            if ch == " ":
                words+=1 
                if broken: 
                    cnt +=1
                    broken = False
        if broken: cnt +=1
        return words-cnt
