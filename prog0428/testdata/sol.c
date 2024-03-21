#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
 
static inline int max(int a, int b){
    if(a > b) return a;
    else return b;
}
 
int k, n;
int ans = 0;
int count_pos = 0;
int count_neg = 0;
int now_count = 0;
 
static inline void update_pos(){
    if(count_pos != 0){
        if(count_pos > k){
            now_count = 1;
        }
        else if(count_pos == k){
            now_count++;
        }
        else{
            now_count = 0;
        }
    }
    ans = max(ans, now_count);
    count_pos = 0;
}
static inline void update_neg(){
    if(count_neg != 0){
        if(count_neg == k){
            if(now_count != 0){
                now_count++;
            }
        }
        else{
            now_count = 0;
        }
    }
    count_neg = 0;
}
 
int main(){
    scanf("%d", &k);
 
    while(scanf("%d", &n) && n != 0){
        if(n > 0){ // pos
            update_neg();
            count_pos++;
        }
        else{ // neg
            update_pos();
            count_neg++;
        }
 
        // printf("%d, %d, %d\n", n, now_count, ans);
    }
    update_pos();
    update_neg();
 
    if(ans == 1) ans = 0;
    printf("%d\n", ans * k);
    return 0;
}