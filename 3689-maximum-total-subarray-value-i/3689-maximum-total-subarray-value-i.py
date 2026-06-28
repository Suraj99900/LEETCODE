class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        # dictSubArr = {}
        # # getting the sub aaray 
        # for iii in range(len(nums)):
        #     for jjj in range(iii,len(nums)):
        #         val= (max(nums[iii:jjj+1])- min(nums[iii:jjj+1]))
        #         if(val == 0):
        #             continue
        #         if(len(dictSubArr) < k and len(dictSubArr)  == 0 ):
        #             dictSubArr[str(nums[iii:jjj+1])] = val
        #         else:
        #             minKey = min(dictSubArr, key=dictSubArr.get)
        #             if(dictSubArr[minKey] < val  and  val != 0):
        #                 dictSubArr.pop(minKey)
        #                 dictSubArr[str(nums[iii:jjj+1])] = val
                    
        # if(len(dictSubArr) <k and len(dictSubArr) > 0):
        #     iPendding = k - len(dictSubArr)
        #     print(iPendding)
        #     for i in range(iPendding):
        #         dictSubArr[str(str(iPendding)+"+"+str(i))]=(min(dictSubArr.values()))
        # # print(dictSubArr)
        # return sum(dictSubArr.values())

        # best = 0

        # for i in range(len(nums)):

        #     currMax = nums[i]
        #     currMin = nums[i]

        #     for j in range(i, len(nums)):

        #         currMax = max(currMax, nums[j])
        #         currMin = min(currMin, nums[j])

        #         best = max(best, currMax - currMin)

        # return best * k
        return (max(nums) - min(nums)) * k