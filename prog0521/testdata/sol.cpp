#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m; cin >> n >> m;
    int arr[n][m];
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) cin >> arr[i][j];

    for(int i = 0; i < n; i++){
        int max_num = INT_MIN;
        for(int j = 0; j < m; j++) max_num = max(max_num, arr[i][j]);
        cout << max_num << " ";
    }

    cout << endl;

    for(int j = 0; j < m; j++){
        int min_num = INT_MAX;
        for(int i = 0; i < n; i++) min_num = min(min_num, arr[i][j]);
        cout << min_num << " ";
    }

    cout << endl;

    return 0;
}
