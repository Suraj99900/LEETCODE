class Solution:
    dictMpped = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        aResultList = []
        mappedString = ''
        bOneRoundTrack=True
        if not digits:
            return []
        mappedString = self.dictMpped[int(digits[0])]
        for jjj in range(len(mappedString)):

            aResultList.append(mappedString[jjj])
        # print(aResultList)
        
        
        for num in range(1,len(digits)):
            newList = []
            mappedString = self.dictMpped[int(digits[int(num)])]
            for old in aResultList:
                for char in mappedString:
                    newList.append(old+char)
            aResultList = newList
        return aResultList
        
        