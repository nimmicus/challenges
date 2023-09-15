class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        companion_indices = {}
        for num in nums:
            if num in companion_indices.keys():
                if companion_indices[num] != i:
                    return [companion_indices[num], i]
            companion_operand = target - num
            companion_indices[companion_operand] = i
            i += 1