#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> dp(max(N + 1, 2));
    dp[0] = 1; dp[1] = 1;
    for (int i = 2; i <= N; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[N] << endl;
    return 0;
}
