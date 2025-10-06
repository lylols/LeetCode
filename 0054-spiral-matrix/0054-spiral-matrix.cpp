class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();        // rows
        int n = matrix[0].size();     // columns
        int top = 0, bottom = m - 1;
        int left = 0, right = n - 1;
        vector<int> result;

        while (top <= bottom && left <= right) {
            // Left → Right
            for (int i = left; i <= right; i++)
                result.push_back(matrix[top][i]);
            top++;
            if (top > bottom) break;

            // Top → Bottom
            for (int i = top; i <= bottom; i++)
                result.push_back(matrix[i][right]);
            right--;
            if (left > right) break;

            //Right → Left
            for (int i = right; i >= left; i--)
                result.push_back(matrix[bottom][i]);
            bottom--;
            if (top > bottom) break;

            // Bottom → Top
            for (int i = bottom; i >= top; i--)
                result.push_back(matrix[i][left]);
            left++;
        }

        return result;
    }
};
