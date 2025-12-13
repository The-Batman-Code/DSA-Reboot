class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        if len(s) != len(t):
            return False
        for i in s:
            a[i] = a.get(i, 0) + 1
        for j in t:
            b[j] = b.get(j, 0) + 1
        return all(a[m] == b.get(m, 0) for m in a)


# TC - O(t+s)
# SC - O(t+s)
