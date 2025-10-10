class Solution {
public:
    int subarraysWithKDistinct(std::vector<int>& nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    int atMost(std::vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        int l = 0, cnt = 0;

        for (int r = 0; r < nums.size(); ++r) {
            freq[nums[r]]++;

            while (freq.size() > k) {
                freq[nums[l]]--;
                if (freq[nums[l]] == 0) {
                    freq.erase(nums[l]);  
                }
                l++;
            }

            cnt += r - l + 1;
        }
        return cnt;
    }
};
