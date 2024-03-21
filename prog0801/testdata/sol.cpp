#include <bits/stdc++.h>
using namespace std;

int main() {
    unsigned int N;
    while (cin >> N) {
        cout << __builtin_popcount(N) << endl;
    }
    return 0;
}
