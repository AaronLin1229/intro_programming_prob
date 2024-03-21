#include <stdio.h>
#include <stdint.h>

int solve(int arr[], int n){
    uint64_t l_bucket = 0, r_bucket = 0;
    uint64_t l_weight = 0, r_weight = 0;

    int p = 0;
    for(int i = 0; i < n; i++){
        r_bucket += arr[i], r_weight += ((p++) * arr[i]);
    }
    for(int i = 0; i < n; i++){
        if(l_weight > r_weight){ 
            return -1;
        }

        if(l_weight == r_weight){
            return i;
        }
        else{
            l_bucket += arr[i], r_bucket -= arr[i];
            l_weight += l_bucket, r_weight -= r_bucket;
        }
    }
    return -1;
}

int main(){
    int n; scanf("%d", &n);
    int arr[n];
    for(int i = 0; i < n; i++) scanf("%d", &arr[i]);
    
    int rtv = solve(arr, n);
    if(rtv != -1) printf("%d\n", rtv + 1);
    else printf("NO\n");
}