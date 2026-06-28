class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iSum = 0
        # aFound = []
        # for iii in range(len(nums)):
        #     for jjj in range(len(nums)):
        #         if iii == jjj:
        #             pass
        #         elif (nums[iii] + nums[jjj]) == target:
        #             return [iii, jjj]

        # optimise solution
        bufferDict ={}
        for i in range(len(nums)):
            if nums[i] in bufferDict:
                return [bufferDict[nums[i]],i]
            else:
                bufferDict[target- nums[i]]=i