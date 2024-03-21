#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
 
static inline int max(int a, int b){
    return (a > b) ? a : b;
}
static inline int min(int a, int b){
    return (a < b) ? a : b;
}
 
void solve(int n){
    int now_num;
    int min_num = INT_MAX, max_num = INT_MIN;
    for(int i = 0; i < n; i++){
        if(scanf("%d", &now_num) == EOF){
            printf("%d\n", min_num);
            return;
        }
        else{
            min_num = min(min_num, now_num);
            max_num = max(max_num, now_num);
        }
    }
    printf("%d\n", max_num);
}
 
int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        solve(n);
    }
}