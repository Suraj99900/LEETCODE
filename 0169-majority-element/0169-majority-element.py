class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # dictData = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dictData.keys():
        #         dictData[nums[i]] = 1
        #     else:
        #         dictData[nums[i]] +=1
        # return max(dictData,key=dictData.get) 
        count = 0
        candidate = None
        
        for num in nums:
            # When count is 0, we pick the current number as the new candidate
            if count == 0:
                candidate = num
            
            # If the number matches the candidate, increment the vote; 
            # otherwise, decrement it
            if num == candidate:
                count += 1
            else:
                count -= 1
        print(count,"---",candidate)
        return candidate