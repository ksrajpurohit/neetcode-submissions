class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T O(nlogn) || S O(1)
        return sorted(s) == sorted(t)