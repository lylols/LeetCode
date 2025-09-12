class Solution {
public:
    int countVowelSubstrings(string word) {
        auto isVowel = [](char c) {
            return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
        };
        
        int n = word.size();
        int count = 0;
        
        // check all substrings
        for(int i=0; i<n; i++){
            if(!isVowel(word[i])) continue;
            unordered_map<char,int> freq;
            for(int j=i; j<n; j++){
                if(!isVowel(word[j])) break;
                freq[word[j]]++;
                if(freq.size()==5) count++;
            }
        }
        return count;
    }
};
