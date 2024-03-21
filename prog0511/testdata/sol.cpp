#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, m; cin >> n >> m;
    int dp[n + 1] = {0};
    dp[0] = 1;

    for(int i = 1; i <= n; i++){
        for(int j = i - 1; j >= 0 && i - j <= m; j--){
            dp[i] += dp[j];
        }
    }
    cout << dp[n] << endl;
}