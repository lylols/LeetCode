class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_map<int, int> freq;
        int ans = nums[0], mx = 0;

        for (int x : nums) {
            freq[x]++;
            if (freq[x] > mx) {
                mx = freq[x];
                ans = x;
            }
        }
        return ans;
    }
};
