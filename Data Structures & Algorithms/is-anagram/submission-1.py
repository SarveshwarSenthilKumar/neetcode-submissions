class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in t:
            if i in s:
                s.replace(i, "")
            else:
                return False
        return True