class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // pair of (matching number, original index)
        unordered_map<int, int> checked;
        for (int i=0; i < nums.size(); i++) {
            if (checked.find(nums[i]) != checked.end()) {
                return {checked[nums[i]], i};
            }
            int match = target - nums[i];
            checked.insert({match, i});
            //cout << checked.find(match) << endl ;
        }
        return {};
    }
};
