from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        arrNew = sorted(set(arr))

        arrData = {}

        rank = 1
        for num in arrNew:
            arrData[num] = rank
            rank += 1

        ans = []

        for num in arr:
            ans.append(arrData[num])

        return ans