class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_sum = float("inf")
        num_len = len(nums)
        nums.sort()
        for i in range(num_len - 1):
            low = i + 1
            high = num_len - 1

            while low < high:
                total = nums[i] + nums[low] + nums[high]
                # print(nums[i], nums[low], nums[high], " -->", total, min_sum, target,  target - total, target - min_sum)
                if abs(target - total) < abs(target - min_sum):
                    min_sum = total
                elif total == target:
                    return total
                # print(i, low, high)
                if total < target:
                    low += 1
                else:
                    high -= 1


        return min_sum