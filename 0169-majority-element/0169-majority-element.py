class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dictData = {}
        for i in range(len(nums)):
            if nums[i] not in dictData.keys():
                dictData[nums[i]] = 1
            else:
                dictData[nums[i]] +=1
        return max(dictData,key=dictData.get) 