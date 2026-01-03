class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int,int> mp;
        for( int i=0; i< nums.size(); i++){
            int t = target - nums[i];
            if (mp.find(t)==mp.end()) mp[nums[i]] = i;
            else return {mp[t],i};
        }
        return {};
    }
};