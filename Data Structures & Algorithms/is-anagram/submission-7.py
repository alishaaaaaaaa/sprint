class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapS = {}
        mapT = {}

        for i in range (len(s)):

            #note that .get(s[i], 0) is needed.
                #if the key doesn't exist, the automatic value will be 0
                #without adding this, a key error will be thrown in the code
            mapS[s[i]] = mapS.get(s[i], 0) + 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1

        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False

        return True