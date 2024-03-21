#include <bits/stdc++.h>
using namespace std;

int main() {
    int r, c;
    cin >> r >> c;
    vector<vector<int>> A(r, vector<int>(c));
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            cin >> A[i][j];

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            bool isGreater = true;
            if (i > 0 && A[i][j] <= A[i-1][j]) isGreater = false;
            if (i < r-1 && A[i][j] <= A[i+1][j]) isGreater = false;
            if (j > 0 && A[i][j] <= A[i][j-1]) isGreater = false;
            if (j < c-1 && A[i][j] <= A[i][j+1]) isGreater = false;
            if (isGreater) cout << A[i][j] << endl;
        }
    }
    return 0;
}
