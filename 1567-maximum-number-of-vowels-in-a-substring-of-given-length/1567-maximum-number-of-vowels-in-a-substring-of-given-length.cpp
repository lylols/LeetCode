class Solution {
public:
    int maxVowels(string s, int k) {
        int left=0, maxx=0, cnt=0;
        for(int rt=0; rt< s.size(); rt++){
            if(s[rt] == 'a' || s[rt] == 'e' || s[rt] == 'i' || s[rt] == 'o' || s[rt] == 'u') { 
                cnt++;
            }
            if(rt-left+1>k){
                if(s[left] == 'a' || s[left] == 'e' || s[left] == 'i' || s[left] == 'o' || s[left] == 'u') {
                    cnt--; 
                }
                left++;
            }

            maxx= max(maxx, cnt);
        }
        return maxx;
    }
};