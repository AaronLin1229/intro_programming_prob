#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int sum = 0;
    while (N > 0) {
        sum += N % 10; // Add the last digit to the sum.
        N /= 10;       // Remove the last digit.
    }
    cout << sum << endl;
    return 0;
}
