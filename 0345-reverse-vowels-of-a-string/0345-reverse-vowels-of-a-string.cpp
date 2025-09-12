class Solution {
public:
    string reverseVowels(string s) {
        int l=0;
        int r= s.size()-1;
        string vow = "aeiouAEIOU";
        while(l<r){
            while(l<r && vow.find(s[l])== string::npos) l++;
            while(l<r && vow.find(s[r])== string::npos) r--;
            swap(s[l],s[r]);
            l++;
            r--;
        }
        return s; 
    }
};