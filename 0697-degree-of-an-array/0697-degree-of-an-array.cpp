class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, int> freq, first;
        int maxFreq = 0, ans = nums.size();

        for (int i = 0; i < nums.size(); i++) {
            int x = nums[i];
            if (!first.count(x)) first[x] = i;
            freq[x]++;

            if (freq[x] > maxFreq) {
                maxFreq = freq[x];
                ans = i - first[x] + 1;
            } else if (freq[x] == maxFreq) {
                ans = min(ans, i - first[x] + 1);
            }
        }
        return ans;
    }
};
