#include <stdio.h>

void selection_sort(int arr[], int n){
    // your code here
}

int main() {
    int n, arr[1024];
    
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    selection_sort(arr, n);

    for(int i = 0; i < n; i++){
        scanf("%d%c", arr[i], (i == n - 1) ? '\n' : ' ');
    }
}
