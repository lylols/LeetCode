class Solution {
public:
    string removeKdigits(string num, int k) {
        string st; // acts like a stack
        for (char ch : num) {
            // Remove larger digits while we can
            while (!st.empty() && st.back() > ch && k > 0) {
                st.pop_back();
                k--;
            }
            st.push_back(ch);
        }

        // Remove remaining digits from the end if needed
        while (k > 0 && !st.empty()) {
            st.pop_back();
            k--;
        }

        // Remove leading zeros
        int start = 0;
        while (start < st.size() && st[start] == '0') {
            start++;
        }

        string result = st.substr(start);
        return result.empty() ? "0" : result;
    }
};
