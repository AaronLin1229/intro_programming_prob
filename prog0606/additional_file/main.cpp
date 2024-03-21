#include <bits/stdc++.h>
using namespace std;

void bubble_sort(int arr[], int n){
    // your code here
}

int main() {
    int n, arr[1024];
    
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    bubble_sort(arr, n);

    for(int i = 0; i < n; i++){
        cout << arr[i] << ((i == n - 1) ? '\n' : ' ');
    }
}
