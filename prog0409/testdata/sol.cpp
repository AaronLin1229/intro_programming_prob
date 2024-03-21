#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> counts(3, 0);
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        counts[x % 3]++;
    }
    cout << counts[0] << " " << counts[1] << " " << counts[2] << endl;
    return 0;
}
