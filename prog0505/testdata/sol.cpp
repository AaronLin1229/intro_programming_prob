#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    int min_diff = INT_MAX;
    for (int i = 1; i < n; i++) min_diff = min(min_diff, A[i] - A[i - 1]);

    cout << min_diff << endl;
    return 0;
}
