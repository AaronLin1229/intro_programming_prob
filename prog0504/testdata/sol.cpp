#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];
    int m; cin >> m;
    int ans[m] = {0};
    for(int i = 0; i < n; i++) ans[arr[i] % m]++;
    for(int i = 0; i < m; i++) cout << ans[i] << endl;
}