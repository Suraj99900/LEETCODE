class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        iSetData = 2
        aData = nums.copy()
        for i in range(len(aData)):
            if(nums.count(aData[i])> 2):
                print(aData[i])
                nums.remove(aData[i])
        print(nums)
            