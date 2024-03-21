#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    long long factorial = 1;
    for (int i = 1; i <= x; ++i) {
        factorial *= i;
    }
    cout << factorial << endl;
    return 0;
}
