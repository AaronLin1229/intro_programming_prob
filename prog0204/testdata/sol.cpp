#include <bits/stdc++.h>
using namespace std;
 
int main(void) {
    long long s, f, t;
    cin >> s >> f >> t;

    long long c = s - t;
    long long b = (f / 2) - (4 * c) - t;
    long long a = t - b;

    cout << a << endl << b << endl << c << endl;
}