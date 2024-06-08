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
    bool isPalindrome(int x) {
        if (x<0) return false;
        std::vector<int> list_x;
        int temp;
        while (x > 0){
            temp = x % 10;
            x = x/10;            
            list_x.push_back(temp);
        }
        auto size_x = list_x.size();
        for(int i = 0; i < size_x; i++ ){
            // printf(" %d %d ", list_x[i], list_x[size_x - i - 1]);
            if (list_x[i] != list_x[size_x - i - 1]) return false;
        }
        return true;
    }
};

int main() {

    auto sol = Solution();

    std::vector<int> vec = {
       121,
       -121,
       10
        };

    

    for (auto x: vec){
        std::cout << x << std::endl;
        auto res = sol.isPalindrome(x);
        // std::cout << "res " << res <<  "\n\n" << std::endl;
        printf("res %d \n\n\n", res);
    }

    return 0;
}