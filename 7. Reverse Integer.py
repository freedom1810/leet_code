def compare_string_number(str1, str2):
    # print(str1, str2)
    res = None
    if len(str1)  < len(str2):
        res = True
    elif len(str1) > len(str2):
        res = False
    else:
        return str1 < str2
    
    return res

def int_to_str_reverse(inp_int):
    """
    inp_int : 1230
    res: 0321
    """
    res = ''
    if inp_int < 0: 
        inp_int = -inp_int
    while inp_int > 0:
        temp = inp_int % 10
        if temp != 0 or (temp  == 0 and len(res) > 0): 
            res += str(temp)
        inp_int //= 10
        
    # print("int_to_str_reverse ", inp_int, res)
    return res

def str_to_int(inp_str):
    res = 0
    for char in inp_str:
        int_char = int(char)
        res = res * 10 + int_char
    # print("str_to_int ", inp_str, res)
    return res

class Solution:
    def reverse(self, x: int) -> int:
        block_on = "2147483647"
        block_bellow = "2147483648"
        
        
        if x < 0:
            x = int_to_str_reverse(x)
            if compare_string_number(x, block_bellow) is not True:
                x = 0
                return x
                
            x = str_to_int(x)
            x = -x
        else:
            x = int_to_str_reverse(x)
            if compare_string_number(x, block_on) is not True:
                x = 0
                return x
                
            x = str_to_int(x)
        return x
    

solution = Solution()



list_input = [
    123,
    -123,
    120,
    1534236469,
    9,
    -9,
    901000
]

for s  in list_input:
    print(f"input {s}")
    
    print(solution.reverse(s))
    
    print('\n\n')