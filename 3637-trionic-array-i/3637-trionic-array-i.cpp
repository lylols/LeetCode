class Solution {
public:
    bool isTrionic(vector<int>& arr) {
        int n = arr.size();
        if (n < 4) return false; 

        int i = 0;

        // 1) first increasing
        int start = i;
        while (i + 1 < n && arr[i] < arr[i + 1]) {
            i++;
        }
        if (i == start) return false;  

        // 2) decreasing
        start = i;
        while (i + 1 < n && arr[i] > arr[i + 1]) {
            i++;
        }
        if (i == start) return false;  

        // 3) increasing again
        start = i;
        while (i + 1 < n && arr[i] < arr[i + 1]) {
            i++;
        }
        if (i == start) return false; 

        return i == n - 1;
    }
};
