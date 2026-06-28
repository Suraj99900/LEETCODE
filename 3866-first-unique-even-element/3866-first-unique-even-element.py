class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        # let first bind the even number dic 
        dictCollection = {}
        for ch in range(len(nums)):
            if(nums[ch]%2 == 0):
                dictCollection[nums[ch]] = dictCollection.get(nums[ch],0)+1
        # print(dictCollection.keys())

        for iii in dictCollection.keys():
            print(iii)
            if(dictCollection[iii] == 1):
                return iii
        return -1