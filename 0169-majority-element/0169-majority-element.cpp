class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt=0;
        int cur= nums[0];
        for(int el : nums){
            if (cnt ==0){
                cur=el;
                cnt+=1;
            }
            else if(el==cur) cnt++;
            else cnt--;
        }
        return cur;
    }
};