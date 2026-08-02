class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        iCounterPresent = len(nums)
        # loop funcation 
        aData = nums.copy()
        for i in range(len(aData)):
            if val == aData[i]:
                nums.remove(val)
                iCounterPresent = iCounterPresent-1
                # aData.append("_")
        # print(iCounterPresent,"---",nums)