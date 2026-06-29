class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        iCount = 0
        for iii in range(len(patterns)):
            if patterns[iii] in word:
                iCount += 1
        return iCount