class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int n = nums.size();
        vector<int> rightMin(n);
        rightMin[n-1] = nums[n-1];

        for (int i = n - 2; i >= 0; --i)
            rightMin[i] = min(nums[i], rightMin[i + 1]);
        
        int leftMax = nums[0];

        for (int i = 0; i < n - 1; ++i) {
            leftMax = max(leftMax, nums[i]);
            if (leftMax <= rightMin[i + 1])
                return i + 1;
        }
        return n - 1;
    }
};
