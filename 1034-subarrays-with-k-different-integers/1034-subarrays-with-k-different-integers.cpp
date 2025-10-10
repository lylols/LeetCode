class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atMost(nums,k)-atMost(nums,k-1);
    }
    int atMost(vector<int>& nums, int k){
        unordered_map<int,int> freq;
        int l=0, cnt=0;
        int n= nums.size();
        for(int r=0; r<n; r++){
            if(freq[nums[r]]==0) k--;
            
            freq[nums[r]]++;
            while(k<0){
                freq[nums[l]]--;
                if(freq[nums[l]]==0) k++;
                l++;
            }
            cnt+= r-l+1;
        }
        return cnt;
    }
};