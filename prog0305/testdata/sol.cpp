#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    if(x % 3 == 0 && x % 5 == 0 && x % 7 != 0) {
        cout << 0;
    } else {
        cout << 1;
    }
    return 0;
}
