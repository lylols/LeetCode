class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[len(letters)-1]<= target:
            return letters[0]
        for a in letters:
            if ord(a)> ord(target):
                return a
            