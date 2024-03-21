#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    vector<int> fib(46);
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= x; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    cout << fib[x] << endl;
    return 0;
}
