#include <bits/stdc++.h>
using namespace std;

void count_pos_neg(int arr[], int n, int res[2]) {
    // your code here
}

int main() {
    int n;
    cin >> n; 

    int arr[10000];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int res[2];
    count_pos_neg(arr, n, res);
    cout << res[0] << " " << res[1] << endl;
}
