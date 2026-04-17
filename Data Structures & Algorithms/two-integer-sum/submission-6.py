class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time O(n) and Space O(n)
        prev_map = {}

        for i, num in enumerate(nums):
            potential_num = target - num
            if potential_num in prev_map:
                return [prev_map[potential_num],i]
            else:
                prev_map[num] = i