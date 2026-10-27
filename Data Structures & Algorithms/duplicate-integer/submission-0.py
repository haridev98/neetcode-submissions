class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        for el in nums:
            if el in counter:
                return True
            else:
                counter.add(el)
        return False
        
        