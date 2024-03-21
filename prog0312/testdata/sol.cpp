#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int d = b * b - 4 * a * c;
    if (d < 0) {
        cout << "0" << endl;
    } else if (d == 0) {
        cout << "1" << endl;
        cout << fixed << setprecision(15) << -b / (2.0 * a) << endl;
    } else {
        cout << "2" << endl;
        double x1 = (-b - sqrt(d)) / (2 * a);
        double x2 = (-b + sqrt(d)) / (2 * a);
        cout << fixed << setprecision(15) << min(x1, x2) << " " << max(x1, x2) << endl;
    }
    return 0;
}
