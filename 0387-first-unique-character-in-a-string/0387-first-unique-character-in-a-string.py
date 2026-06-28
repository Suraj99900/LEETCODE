class Solution:
    def firstUniqChar(self, s: str) -> int:
        # in brute force method 
        # for iEle in range(len(s)):
        #     # print(s)
        #     news = s.replace(s[iEle],"",1)
        #     # print(news)
        #     # print(s[iEle])
        #     if s[iEle] not in news:
        #         return iEle
        
        # return -1

        # optimised way ti fix 
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for ch in range(len(s)):
            if freq[s[ch]]  ==1:
                return ch
        return -1

        