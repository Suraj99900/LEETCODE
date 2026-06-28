class Solution:
    def firstUniqChar(self, s: str) -> int:
        # in brute force method 
        for iEle in range(len(s)):
            # print(s)
            news = s.replace(s[iEle],"",1)
            # print(news)
            # print(s[iEle])
            if s[iEle] not in news:
                return iEle
        
        return -1

        