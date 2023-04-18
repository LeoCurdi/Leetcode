

#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <sstream>
#include <chrono>
#include <iomanip>
#include <ctime>

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


class Solution {
public:
    int distinctAverages(vector<int>& nums) {
        // get size
        int numsSize = nums.size();

        // sort it
        sort(nums.begin(), nums.end());

        // create a vector to store averages
        vector<double> av;

        // run it
        for (int i = 0; i < numsSize / 2; i++) {
            double average = (nums[i] + nums[nums.size() - 1 - i]) / 2.0;

            int dupe = 0;

            // check for duplicate
            for (int j = 0; j < av.size(); j++) {
                if (av[j] == average) {
                    dupe = 1;
                }
            }

            // insert
            if (dupe == 0) av.push_back(average);
        }

        return av.size();
    }
};

int main(void) {



    return 0;
}