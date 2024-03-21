#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> A(n, vector<int>(m)), B(m, vector<int>(k)), C(n, vector<int>(k));

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> A[i][j];

    for (int i = 0; i < m; ++i)
        for (int j = 0; j < k; ++j)
            cin >> B[i][j];

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < k; ++j)
            for (int r = 0; r < m; ++r)
                C[i][j] += A[i][r] * B[r][j];

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < k; ++j)
            cout << C[i][j] << " ";
        cout << endl;
    }
    return 0;
}
