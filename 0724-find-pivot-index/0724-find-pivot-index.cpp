class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total =0;
        for( int n: nums) total += n;

        int lsum=0;
        int rsum = total;
        for(int i=0; i< nums.size(); i++){
            //lsum+=nums[i];
            rsum -= nums[i];
            if (lsum==rsum) return i;
            lsum+= nums[i];
        }
        return -1;
    }
};