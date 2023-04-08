#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> targets;
        int len = nums.size();

        for(int i=0; i<len; i++) {
            int temp = nums.at(i);
            targets[target - temp] = i;
        }

        vector<int> result;
        for(int i=0; i<len; i++) {
            if(targets.count(nums.at(i)) > 0) {
                int pos = targets.at(nums.at(i));
                if(pos != i) {
                    result.push_back(pos);
                    result.push_back(i);

                    return result;
                }
            }
        }
        return result;

    }
};