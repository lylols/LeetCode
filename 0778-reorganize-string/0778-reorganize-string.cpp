class Solution {
public:
    string reorganizeString(string s) {
        int n= s.size();
        int freq[26]= {0};
        int maxi = 0, maxc=0;

        //storing freq
        for(auto c: s){
            freq[c-'a']++;
            if(freq[c-'a']> maxi){
                maxi = freq[c-'a'];
                maxc = c-'a';
            }
        }

        if( maxi> (n+1)/2) return "";

        //start filling
        string res(n,' ');
        int idx=0;

        for(idx;idx<n; idx+=2){
            if(freq[maxc]>0){
                res[idx]= 'a'+maxc;
                freq[maxc]--;
            }
            else break;
        }

        for(int i =0; i<26; i++){
            while( freq[i]>0){
                if(idx>=n) idx=1;
                res[idx]= 'a'+i;
                idx+=2;
                freq[i]--;
            }
        }
        return res;
    }
};