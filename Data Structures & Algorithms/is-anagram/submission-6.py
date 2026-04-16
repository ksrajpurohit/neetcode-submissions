class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T O(n + m) || S O(n + m)
        if len(s) != len(t): return False

        frequency_map = {}

        for ch in s:
            frequency_map[ch] = frequency_map.get(ch, 0) + 1

        for ch in t:
            frequency_map[ch] = frequency_map.get(ch, 0) - 1

        for k, v in frequency_map.items():
            if v > 0:
                return False

        return True
