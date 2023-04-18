

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
    int distributeCandies(vector<int>& candyType) {
        int result = 0, dupe = 0;
        int a = 0, b = 0;
        vector<int> unique;

        // sort candy type
        sort(candyType.begin(), candyType.end());

        for (; a < candyType.size(); a++) {
            if (a == 0 || candyType[a] != candyType[a - 1]) {
                unique.push_back(candyType[a]);
            }
        }

        int n = candyType.size() / 2;
        if (n > unique.size()) return unique.size();
        else return n;
    }
};

int main(void) {



    return 0;
}