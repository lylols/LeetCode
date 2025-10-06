class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        vector<int> prefix_array(n);
        prefix_array[0] = pref[0];
        for (int i = 1; i < n; i++) {
            prefix_array[i] = pref[i] ^ pref[i - 1];
        }
        return prefix_array;
    }
};