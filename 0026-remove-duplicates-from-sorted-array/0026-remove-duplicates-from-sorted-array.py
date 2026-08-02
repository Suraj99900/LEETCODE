class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # icounter
        Counter =0
        aData = nums.copy()
        for i in range(len(aData)):
            if (aData[i] in aData[i+1:]):
                nums.remove(aData[i])
        print(nums)