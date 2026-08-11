class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0 
        uniqueSet = set()
        res = 0

        for r in range(len(s)):
            while s[r] in uniqueSet:
                uniqueSet.remove(s[l])
                l+=1
            uniqueSet.add(s[r])
            res = max(res, r-l+1)

        return res

