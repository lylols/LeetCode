class Solution {
public:
    string sortVowels(string s) {
        string vow = "aeiouAEIOU";
        vector<char> vs;

        for(char ch: s){
            if(vow.find(ch) != string :: npos){
                vs.push_back(ch);
            }
        }

        sort(vs.begin(), vs.end());

        int idx=0;
        for(char &ch: s){
            if(vow.find(ch) != string :: npos){
                ch= vs[idx++]; 
            }
        }
        return s;
    }
};