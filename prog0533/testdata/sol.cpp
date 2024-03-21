#include <bits/stdc++.h>
using namespace std;

int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> field(n);
    for (int i = 0; i < n; i++) {
        cin >> field[i];
    }

    auto isValid = [&](int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    };

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (field[i][j] == '.') {
                int count = 0;
                for (int k = 0; k < 8; k++) {
                    int ni = i + dx[k], nj = j + dy[k];
                    if (isValid(ni, nj) && field[ni][nj] == '*') {
                        count++;
                    }
                }
                field[i][j] = '0' + count;
            }
        }
    }

    for (const auto& row : field) {
        cout << row << endl;
    }

    return 0;
}
