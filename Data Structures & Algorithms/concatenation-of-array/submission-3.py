class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # T O(n) || S O(n)
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
