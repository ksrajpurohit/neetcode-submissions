class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T O(nlogn + mlogm) || S O(1)
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)