class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        prev = 0
        counter = 0

        # This is working with a blind assumption that if two elements are not equal
        # then sum of its adjacent will make it palimndroms
        while left <= right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                prev = nums[left]
                left += 1
                counter += 1
                nums[left] = nums[left] + prev
            elif nums[left] > nums[right]:
                prev = nums[right]
                right -= 1
                counter += 1
                nums[right] = nums[right] + prev
                    
        return counter


        