class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        stack<pair<char,int>> stk; // store {color, time}
        int total = 0;

        for (int i = 0; i < colors.size(); i++) {
            if (!stk.empty() && stk.top().first == colors[i]) {
                total += min(stk.top().second, neededTime[i]); 
                stk.top().second = max(stk.top().second, neededTime[i]); 
            } else {
                stk.push({colors[i], neededTime[i]});
            }
        }
        return total;
    }
};
