#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    while(b != 0){
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    long long a, b;
    cin >> a >> b;
    long long ans = a * b / gcd(a, b);
    cout << ans << endl;
    return 0;
}
