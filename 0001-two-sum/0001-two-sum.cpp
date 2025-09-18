class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mpp;
        for(int i =0; i< nums.size(); i++){
            int t = target-nums[i];
            if(mpp.find(t)!= mpp.end()) return {mpp[t],i};
            else mpp[nums[i]]=i;
        }
        return {};
    }
};