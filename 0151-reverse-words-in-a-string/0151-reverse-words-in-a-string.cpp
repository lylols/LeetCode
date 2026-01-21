class Solution {
public:
    string reverseWords(string s) {
        vector<string> vec;
        string wrd = "";
        for(int i =0; i< s.size(); i++){
            if(s[i]!= ' '){
                wrd+= s[i];
            }
            else if(!wrd.empty()){
                vec.push_back(wrd);
                wrd="";
            }
        }
        if (!wrd.empty()) vec.push_back(wrd);
        reverse(vec.begin(), vec.end());
        string res = "";
        for(int i =0; i< vec.size(); i++){
            res+= vec[i];
            if(i!= vec.size()-1) res+= " ";
        }
        return res;
    }
};