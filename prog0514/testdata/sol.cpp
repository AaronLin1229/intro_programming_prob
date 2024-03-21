#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    bool sorted = is_sorted(a.begin(), a.end());
    cout << (sorted ? "YES" : "NO") << endl;
    return 0;
}
