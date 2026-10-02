class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #this is lowkey cheating -- it's a built-in python function
        return Counter(s) == Counter(t)