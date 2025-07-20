class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.find_bound(nums, target, True)
        upper = self.find_bound(nums, target, False) 
        return [lower, upper]

    def find_bound(self, nums: List[int], target: int, lower: bool) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:

            mid = (left + right) // 2
            print(left, right, mid, nums[mid])
            if nums[mid] == target:
                if lower:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    else:
                        right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    else:
                        left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1