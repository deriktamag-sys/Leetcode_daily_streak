#num = [2,7,11,15,19,5]
#target = 9
class Solution:
    def twoSum(self, nums: list[int], target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]
obj = Solution()
nums = [2,7,11,15,19,5]
target = 9
output = obj.twoSum(nums, target)
print(f"Output: {output}")