class Solution {
public:
    int reverse(int x) {
        long long int rev=0;
        int neg = (x<0)? -1:1;
        //x = abs(x);
        while (x){
            rev = rev*10 + x%10;
            x /=10;
        }
        return (rev < INT_MIN || rev > INT_MAX) ? 0 : (int)rev;
    }
};