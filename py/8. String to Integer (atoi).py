class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        check_ = False
        status_ = True
        for char in s:
            if char in "0123456789":
                res = res*10 + int(char)
                check_ = True
            elif char == ' ':
                if check_:
                    break
                continue
            elif char in "+-":
                # print(check_)
                if check_:
                    break
                else:
                    if char == "+":
                        status_ = True
                    else:
                        status_ = False
                    check_ = True
            else:
                break
            
        block = 2147483648
        
        if not status_:
            res = -res
 
                
        if res > 2**31 -1:
            return 2**31 -1
        elif res < -2**31:
            return  -2**31
        
        return res
        
solution = Solution()

list_input = [
    "42",
    "   -042",
    "1337c0d3",
    "0-1",
    "words and 987",
    "-91283472332",
    "   +0 123"


]

for s  in list_input:
    print(f"input {s}")
    
    print(solution.myAtoi(s))
    
    print('\n\n')