class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T O(nlogn) || S O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        