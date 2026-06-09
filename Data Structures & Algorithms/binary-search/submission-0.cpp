class Solution {
public:
    int searchHelper(vector<int>& nums, int target, int left, int right) {
        if (left > right) return -1;
        if (left==right && nums[left]!=target) return -1; 

        int mid = (right + left) / 2;
        cout << mid << endl;
        if (nums[mid] == target) 
            return mid;
        else if (nums[mid] < target) 
            return searchHelper(nums, target, mid+1, right);
        else
            return searchHelper(nums, target, left, mid);
        
    }

    int search(vector<int>& nums, int target) {
        return searchHelper(nums, target, 0, nums.size()-1);
    }
};
