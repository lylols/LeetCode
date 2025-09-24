class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> keys;
        for( auto word : strs){
            //string temp = word;
            string sorted = word;
            sort(sorted.begin(),sorted.end());
            keys[sorted].push_back(word);
        }
        vector<vector<string>> res;
        for(auto it: keys){
            res.push_back(it.second);
        }
        return res;
    }
};