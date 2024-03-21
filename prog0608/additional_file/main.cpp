#include <bits/stdc++.h>
using namespace std;

void selection_sort(int arr[], int n){
    // your code here
}

int main() {
    int n, arr[1024];
    
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    selection_sort(arr, n);

    for(int i = 0; i < n; i++){
        cout << arr[i] << ((i == n - 1) ? '\n' : ' ');
    }
}
