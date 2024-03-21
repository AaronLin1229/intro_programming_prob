#include <bits/stdc++.h>
using namespace std;

int removeDuplicates(vector<int>& A) {
    if (A.empty()) return 0;
    
    int m = 0;
    for (int i = 1; i < A.size(); ++i) {
        if (A[i] != A[m]) {
            m++;
            A[m] = A[i];
        }
    }
    return m + 1;
}

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int m = removeDuplicates(A);
    cout << m << endl;
    for (int i = 0; i < m; ++i) {
        cout << A[i] << " ";
    }
    cout << endl;
    return 0;
}
