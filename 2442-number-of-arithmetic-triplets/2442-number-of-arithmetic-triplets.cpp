class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int cnt=0;
        unordered_map<int, int> mpp;
        for(int a: nums){
            mpp[a]++;
        }
        for(int i=2; i<nums.size(); i++){
            if (mpp.find(nums[i]-diff)!= mpp.end() && mpp.find(nums[i]-2*diff)!= mpp.end()) cnt++;
        }
        return cnt;
    }
};