#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, m, k; cin >> n >> m >> k;
    int dp[n + 1] = {0}; dp[0] = 1;
    bool cannot_use[n + 1] = {false};
    for(int i = 0; i < k; i++){
        int d; cin >> d; cannot_use[d] = true;
    }

    for(int i = 1; i <= n; i++){
        if(cannot_use[i]){
            dp[i] = 0;
        }
        else{
            for(int j = i - 1; j >= 0 && i - j <= m; j--){
                dp[i] += dp[j];
            }
        }
    }
    cout << dp[n] << endl;
}