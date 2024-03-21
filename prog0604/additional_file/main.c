#include <stdio.h>

void count_pos_neg(int arr[], int n, int res[2]) {
    // your code here
}

int main() {
    int n;
    scanf("%d", &n);

    int arr[10000];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    int res[2];
    count_pos_neg(arr, n, res);
    printf("%d %d\n", res[0], res[1]);
}
