class Solution {
public:
    long long countVowels(string word) {
        long long cnt=0;
        for(int i =0; i< word.size(); i++){
            char c= word[i];
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                cnt += (i+1)*(word.size()-i);
            }
        }
        return cnt;
    }
};