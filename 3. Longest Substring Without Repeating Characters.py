class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ''
        longest_length = 0
        for char in s:
            if char in res:
                
                longest_length = max(longest_length, len(res))
                index = res.index(char)
                res = res[index + 1:]
            res = res + char
        longest_length = max(longest_length, len(res))
        return longest_length