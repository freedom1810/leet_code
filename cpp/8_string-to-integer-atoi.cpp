#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;


const int INT_MAX = 2147483647;
const int INT_MIN = -2147483648;
const int LAST_MAX = 7;
const int LAST_MIN = 8;

class Solution {
public:
    int myAtoi(string s) {
        int res = 0;
        bool check_ = false;
        bool status_ = true;
        string default_int = "1234567890";
        string dau = "+-";
        
        int num = 0;
        for (char char_:s){
            if (default_int.find(char_) != std::string::npos){
                num = char_ - '0';
                
                if((res>INT_MAX/10 && status_ == true) ||
                 (res == INT_MAX/10 && status_ == true && num >= LAST_MAX))
                {
                    return INT_MAX;
                }

                if((-res < INT_MIN/10 && status_ == false) || (-res == INT_MIN/10 && status_ == false && num >= LAST_MIN))
                {
                    return INT_MIN;
                }
                res = res*10 +  + num;
                check_ = true;
            } else if (char_ == ' '){
                if (check_) break;
                continue;
            } else if (dau.find(char_) != std::string::npos){ 
                if (check_) break;
                else {
                    if (char_ == '+'){
                        status_ = true;
                    } else status_ = false;
                    check_ = true;
                }
            } else break;
        }

    if (!status_) res = -res;
    return res;
    }
};

int main() {

    auto sol = Solution();

    std::vector<string> vec = {
        "42",
        "   -042",
        "1337c0d3",
        "0-1",
        "words and 987",
        "-91283472332",
        "   +0 123",
        "2147483646",
        "-91283472332"
        };

    
    
    for (auto x: vec){
        std::cout << x << std::endl;
        auto res = sol.myAtoi(x);
        // std::cout << "res " << res <<  "\n\n" << std::endl;
        printf("res %d \n\n\n", res);
    }

    return 0;
}