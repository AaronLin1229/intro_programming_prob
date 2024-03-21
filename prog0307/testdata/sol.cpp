#include <bits/stdc++.h>
using namespace std;

int main() {
    int h1, m1, h2, m2;
    cin >> h1 >> m1;
    cin >> h2 >> m2;
    
    int t1 = h1 * 60 + m1;
    int t2 = h2 * 60 + m2;
    int diff = t2 - t1;

    if (diff < 0) {
        diff += 24 * 60;
    }

    int h = diff / 60;
    int t = diff % 60;

    cout << h << " " << t << endl;
}
