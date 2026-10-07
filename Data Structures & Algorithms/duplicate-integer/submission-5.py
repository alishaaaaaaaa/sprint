class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # this solution uses a dictionary -- not necessary because we      
        # don't need to know the values, we just need to know if it exists 
        # in the set. a hashset would be better
        countMap = {}

        for num in nums:
            if num not in countMap:
                countMap[num] = 1
            else:
                return True
        return False

        