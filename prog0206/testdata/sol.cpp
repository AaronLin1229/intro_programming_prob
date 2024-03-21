#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, d, e, f;
    cin >> a >> b >> c;
    cin >> d >> e >> f;

    // Inner product
    int innerProduct = a*d + b*e + c*f;
    cout << innerProduct << endl;

    // Cross product
    int x = b*f - c*e;
    int y = c*d - a*f;
    int z = a*e - b*d;
    cout << x << " " << y << " " << z << endl;

    return 0;
}
