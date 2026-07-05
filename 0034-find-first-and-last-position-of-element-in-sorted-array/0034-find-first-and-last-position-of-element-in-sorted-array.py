class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find first occurrence
        def findFirst():
            left = 0
            right = len(nums) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2
                print("right=",right)
                print("left=",left)
                print("nums[mid]=", mid)
                if nums[mid] == target:
                    first = mid          # Save answer
                    right = mid - 1      # Continue searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return first

        # Find last occurrence
        def findLast():
            left = 0
            right = len(nums) - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    last = mid           # Save answer
                    left = mid + 1       # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last

        first = findFirst()

        if first == -1:
            return [-1, -1]

        last = findLast()
        return [first, last]
