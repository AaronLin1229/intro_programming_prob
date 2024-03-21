#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    int maxIndex = 0;
    for (int i = 1; i < n; i++) {
        if (A[i] > A[maxIndex]) {
            maxIndex = i;
        }
    }

    cout << maxIndex + 1<< endl;
    return 0;
}
