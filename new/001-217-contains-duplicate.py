class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > 1:
                return True

        return False


# TC - O(n)
# SC - O(n)


# Alternate -
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
