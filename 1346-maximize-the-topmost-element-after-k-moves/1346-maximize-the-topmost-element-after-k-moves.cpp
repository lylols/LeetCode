class Solution {
public:
    int maximumTop(vector<int>& nums, int k) {
        if(nums.size()==1 && k%2!=0) return -1;
        if(k==1) return nums[k];
        int mx=nums[0];
        for(int i=0; i<k-1 && i<nums.size(); i++){
            mx= max(mx,nums[i]);
        }
        if(k<nums.size())mx= max(mx,nums[k]);
        return mx;
    }
};