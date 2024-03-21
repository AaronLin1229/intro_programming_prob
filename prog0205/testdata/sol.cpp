#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int determinant = a*d - b*c;
    cout << determinant << endl;
    return 0;
}
