class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int,int> freq;
        long long summ=0;
        int l=0;
        long long maxx=0;
        for(  int i =0;i< nums.size(); i++){
            freq[nums[i]]++;
            summ+= nums[i];
            while(freq[nums[i]] ==2){
                freq[nums[l]]--;
                summ-=nums[l];
                l++;
            }
            maxx= max(maxx,summ);
        }
        return maxx;
    }
};