class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        unordered_map<int,int> freq;
        int maxi=0;
        int maxel= -1;
        for(auto s: nums){
            freq[s]++;
            if (s%2==0){
                if (freq[s]>maxi){
                    maxi = freq[s];
                    maxel= s;
                }
                else if (freq[s]==maxi){
                    maxel= min(maxel,s);
                }
            }
        }
        return maxel;
    }
};