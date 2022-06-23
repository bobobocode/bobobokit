class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            a = nums[i]
            find = target - a
            if find in nums_map:
                return [nums_map[find], i]
            else:
                nums_map[a] = i
