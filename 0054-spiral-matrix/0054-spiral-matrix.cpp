class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {

        vector<int> result;

        int m = matrix.size();      // number of rows
        int n = matrix[0].size();   // number of columns

        int count = 0;
        int total = m * n;

        int top = 0;
        int down = m - 1;
        int left = 0;
        int right = n - 1;

        while (count < total) {

            // Left to Right
            for (int i = left; count < total && i <= right; i++) {
                result.push_back(matrix[top][i]);
                count++;
            }
            top++;

            // Top to Bottom
            for (int i = top; count < total && i <= down; i++) {
                result.push_back(matrix[i][right]);
                count++;
            }
            right--;

            // Right to Left
            for (int i = right; count < total && i >= left; i--) {
                result.push_back(matrix[down][i]);
                count++;
            }
            down--;

            // Bottom to Top
            for (int i = down; count < total && i >= top; i--) {
                result.push_back(matrix[i][left]);
                count++;
            }
            left++;
        }

        return result;
    }
};
