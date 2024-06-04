"""
crate numRows-1 sub_string
state = 0 # 0~down, 1~up

for all char in s:
    update index according to state
    add char to sub_string[index]
    
    update state according to index
    if index == numRows or index == 0 -> switch state
    
        row 
        0      1           7              14 
        1        2       6   8         13
        2          3   5       9    12
        3            4           10 
state:         0 0 0 1 1 1 0 0 0 1  1  1  0

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        state = 0 # 0~down, 1~up
        last_index_updated = 0
        res = ['' for i in range(numRows)]
        
        if s == '' or numRows == 1:
            return s
        
        res[0] += s[0]
        for char in s[1:]:
            if state == 0:
                last_index_updated += 1
            if state == 1:
                last_index_updated -= 1
                
            res[last_index_updated] += char
            
            if last_index_updated == 0:
                state = 0
            elif last_index_updated == numRows - 1:
                state = 1
        
        res_s = ''.join(res)
        return res_s

solution = Solution()



list_input = [
    ("PAYPALISHIRING", 3),
    ("PAYPALISHIRING",  4),
    ("AB", 1)
]

for s, num_row  in list_input:
    print(f"input {s}")
    
    print(solution.convert(s, num_row))
    
    print('\n\n')