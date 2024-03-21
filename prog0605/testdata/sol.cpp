#include <bits/stdc++.h>
using namespace std;

typedef long long int;

int C(int n, int k) {
    int result = 1;
    if (k > n - k) {
        k = n - k;
    }
    for (int i = 0; i < k; ++i) {
        result *= (n - i);
        result /= (i + 1);
    }
    return result;
}

int main() {
    int n, k;
    cin >> n >> k;
    cout << C(n, k) << endl;
    return 0;
}
