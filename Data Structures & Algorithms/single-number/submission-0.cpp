class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for (const auto x : nums) {
            result = result ^ x;
        }
        return result;
    }
};
