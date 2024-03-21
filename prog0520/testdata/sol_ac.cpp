#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int arr[n]; for(int i = 0; i < n; i++) cin >> arr[i];

    int max_num = INT_MIN;
    for(int i = 0; i < n; i++){
        int sum = 0;
        for(int j = i; j < n; j++){
            sum += arr[j];
            max_num = max(max_num, sum);
        }
    }

    cout << max_num << endl;
}