#include <iostream>
#include <vector>
using namespace std;

// bool compare_string_number(std::string str1, std::string str2){
//     bool res = false;
//     if (str1.length() < str2.length()){
//         // cout << "case 1" << endl;
//         res = true;
//     } 
//     else if (str1.length() > str2.length()){
//         res = false;
//         // cout << "case 2" << endl;
//     }
//     else{
//         char char1, char2;
//         int temp1, temp2;
//         for (int i = 0; i < str1.length(); i++){
//             char1 = str1[i];
//             char2 = str2[i];
//             temp1 = char1  - '0';
//             temp2 = char2  - '0';
//             if (temp1 < temp2){
//                 res = true;
//                 break;
//             } else if (temp1 > temp2){
//                 res = false;
//                 break;
//             } 

//         }
//     }
//     return res;
// }


// std::string int_to_str_reverse(int x){
//     /*
//     inp_int : 1230
//     res: 0321
//     */
    
//     std::string res;

//     if (x<0){
//         x = -x;
//     }
//     while (x>0){
//         int temp = x % 10;
//         if ((temp != 0) || ( (temp == 0 ) && res.length() > 0 )){
//             res = res + std::to_string(temp);
//         }
//         x = x / 10;
//     }
//     // cout << "int_to_str_reverse res " << res << endl;
//     return res;
// }

// int str_to_int(std::string str_x){
//     int res = 0;
//     // cout << "str_to_int str_x " << str_x << endl;
//     for (auto char_x: str_x){
//         // cout << "str_to_int char_x " << char_x << endl;
//         // int temp = static_cast<int>(char_x);
//         int temp = char_x  - '0';
//         // cout << "str_to_int temp " << temp << endl;
//         res = res*10 + temp;
//     }
//     // cout << "str_to_int res " << res << endl;
//     return res;
// }

// class Solution {
// public:
//     int reverse(int x) {
//         std::string block_on = "2147483647";
//         std::string block_bellow = "2147483648";
//         if (x == -2147483648){
//             x = 0;
//             return x;
//         }

//         if (x<0){
//             x = -x;
//             std::string str_x = int_to_str_reverse(x);
//             // std::cout<<  str_x << std::endl;
//             if (compare_string_number(str_x, block_bellow))
//             {
//                 x = str_to_int(str_x);
//                 x = -x;
//             } else{
//                 x = 0;
//                 return x;
//             }
                
//         } else{
//             std::string str_x = int_to_str_reverse(x);
//             // std::cout<<  str_x << std::endl;
//             if (compare_string_number(str_x, block_on))
//             {
//                 x = str_to_int(str_x);
//             } else{
//                 x = 0;
//                 return x;
//             }
//         }
//         return x;
//     }
// };


int INT_MAX = 2147483647;
int INT_MIN = -2147483648;
class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while(x)
        {
            int digit = x%10;
            x = x/10;

            if(ans>INT_MAX/10||ans<INT_MIN/10)
            {
                return 0;
            }
            ans = ans*10+digit;
        }

        return ans;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;

    auto sol = Solution();

    std::vector<int> vec = {
        123,
        -123,
        120,
        1534236469,
        9,
        -9,
        901000,
        -2147483648

        };

    for (auto x: vec){
        std::cout << x << std::endl;
        auto res = sol.reverse(x);
        std::cout << res <<  "\n\n" << std::endl;
    }

    return 0;
}