# def checkPalindrome(sub_str):
#     start_index = 0 
#     end_index = len(sub_str) - 1
#     res = True
#     while start_index < end_index:
#         if sub_str[start_index] != sub_str[end_index]:
#             res = False
#             break
#         start_index += 1
#         end_index -= 1
#     return res

# class Solution:
    
#     def longestPalindrome(self, s: str) -> str:
#         sub_str = s[0]
#         # print(range(len(s), 0, -1))
#         for i in range(len(s), 0, -1):
#             # print(i)
#             for j in range(0, len(s)-i+1):
#                 # print(i, j)
#                 sub_str = s[j:j+i]
#                 # print(sub_str)
#                 if checkPalindrome(sub_str):
#                     return sub_str
#         return sub_str



"""
for every char in string
expand left and right to find longestPalindrome

s = babad

char = b
b
ba 

char = a
bab
"""
def findPalindrome(index, s):
    sub_str = ''
    len_str = len(s)
    if index == len_str - 1:
        sub_str = s[index]
    
    left_index = index - 1
    right_index = index + 1

    while left_index >= 0 and right_index <= len_str - 1:
        if s[left_index] == s[right_index]:
            left_index -= 1
            right_index += 1
        else:
            break
    
    sub_str_1 = s[left_index + 1 : right_index]
    
    
    left_index = index
    right_index = index + 1

    while left_index >= 0 and right_index <= len_str - 1:
        if s[left_index] == s[right_index]:
            left_index -= 1
            right_index += 1
        else:
            break
        
    sub_str_2 = s[left_index + 1 : right_index]
    
    if len(sub_str_1) > len(sub_str_2):
        sub_str = sub_str_1
    else:
        sub_str = sub_str_2
    return sub_str

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            temp_res = findPalindrome(i, s)
            # print(i, temp_res)
            if len(temp_res) > len(res):
                res = temp_res
        return res

solution = Solution()


# s = 
# s = 
# s = "a"
list_input = [
    "babad",
    "cbbd",
    "a",
    "asdf",
    "bb"
]

for s in list_input:
    print(f"input {s}")
    
    print(solution.longestPalindrome(s))
    
    print('\n\n')