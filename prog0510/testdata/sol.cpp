#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, k; cin >> n >> k
    int dp[n + 1] = {0};
    bool cannot_use[n + 1] = {false};
    for(int i = 0; i < k; i++){
        int dummy; cin >> dummy;
        cannot_use[dummy] = true;
    }

    dp[0] = 1;
    dp[1] = cannot_use[1] == false ? 1 : 0;
    for(int i = 2; i <= n; i++){
        if(cannot_use[i] == true) dp[i] = 0;
        else dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[n] << endl;
}