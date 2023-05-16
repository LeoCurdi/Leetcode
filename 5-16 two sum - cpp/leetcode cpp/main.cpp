

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
using std::find;


/*
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    less than O(n^2)
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // create a copy of the vector
        vector<int> sortedNums;
        for (int i = 0; i < nums.size(); i++) sortedNums.push_back(nums[i]);

        // sort the copy
        sort(sortedNums.begin(), sortedNums.end());

        // set up left and right pointers
        int l = 0, r = sortedNums.size() - 1;

        // if r is greater than n, move r
        while (sortedNums[r] > target) r--;
        
        // move until we have the solution
        while (sortedNums[l] + sortedNums[r] != target) {
            
            // if sum is less than n, move l
            if (sortedNums[l] + sortedNums[r] < target) l++;

            // else if sum is more than n, move r
            else if (sortedNums[l] + sortedNums[r] > target) r--;
        }

        // now l + r == n, so find the indices of the solution values in the original vector
        int a = 0, b = 0;
        while (nums[a] != sortedNums[l]) a++;
        while (nums[b] != sortedNums[r]) b++;

        // if the solution is two of the same number, we need to return indices of each occurence
        if (a == b) {
            b++;
            while (nums[b] != sortedNums[r]) b++;
        }

        // return solution vector
        vector<int> indices = { a, b };
        return indices;
    }
};

int main(void) {
    Solution a;
    vector<int> nums = { 3,2,3 };
    vector<int> indices = a.twoSum(nums, 6);
    cout << indices[0] << ", " << indices[1];

    return 0;
}