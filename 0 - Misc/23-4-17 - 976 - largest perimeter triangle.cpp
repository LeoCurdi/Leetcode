

#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <sstream>
#include <chrono>
#include <iomanip>
#include <ctime>
#include <algorithm> // for using sort

using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::fstream;
using std::ostream;
using std::string;
using std::vector;
using std::stringstream;
using std::sort;


class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        int result = 0;

        // sort the array
        sort(nums.begin(), nums.end());

        for (int i = nums.size() - 3; i >= 0; i--) { // iterate through each pissible combo of sides

            if (nums[i] + nums[i + 1] > nums[i + 2] && result == 0) { // check if it will make a valid triangle: big side has to be shorter than 2 smaller sides

                result = nums[i] + nums[i + 1] + nums[i + 2]; // calculate and return the sum
            }
        }

        return result;
    }
};

int main(void) {



    return 0;
}