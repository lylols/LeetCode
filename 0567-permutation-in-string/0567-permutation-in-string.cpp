class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        if (m > n) return false;
        vector<int> freq1(26, 0);  // s1
        vector<int> freq2(26, 0);  // s2
  

        for (char c : s1) freq1[c - 'a']++;

        for (int i = 0; i < m; i++)  freq2[s2[i] - 'a']++;

        if (freq1 == freq2) return true;

        for (int i = m; i < n; i++) {
            freq2[s2[i] - 'a']++;     
            freq2[s2[i - m] - 'a']--;   

            if (freq1 == freq2) return true;
        }

        return false;
    }
};