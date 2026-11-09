class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            second = target - val
            if second in seen:
                return [seen[second], i]
            seen[val] = i 