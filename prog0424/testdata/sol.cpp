#include <bits/stdc++.h>
using namespace std;

int main() {
    int k;
    cin >> k;
    for(int i = 1; i <= k; ++i) {
        for(int j = 1; j <= i - 1; ++j) cout << " ";
        for(int j = 1; j <= k - i + 1; j++) cout << "*";
        cout << endl;
    }
    return 0;
}
