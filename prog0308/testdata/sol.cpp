#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, score = 0;
    cin >> N;
    if (N > 40) {
        score = 100;
    } else {
        for (int i = 1; i <= N; ++i) {
            if (i <= 10) score += 6;
            else if (i <= 20) score += 2;
            else score += 1;
        }
    }
    cout << score << endl;
    return 0;
}
