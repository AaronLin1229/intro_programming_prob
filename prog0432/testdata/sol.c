#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
 
int main(){
    int n; scanf("%d", &n);
    int last, now; scanf("%d", &last);
    if(n == 1){
        printf("%d %d %d\n", last, 1, last);
        return 0;
    }
 
    scanf("%d", &now);
    int max_sum = last + now, max_len = 2, max_first = last;
    int now_sum = max_sum, now_len = max_len, now_first = max_first;
    int last_d = now - last;
    for(int i = 2; i < n; i++){
        last = now; scanf("%d", &now);
        int d = now - last;
        if(d == last_d){
            now_sum += now;
            now_len += 1;
        }
        else{
            now_sum = last + now;
            now_len = 2;
            now_first = last;
            last_d = d;
        }
 
        if(now_sum > max_sum){
            max_sum = now_sum;
            max_len = now_len;
            max_first = now_first;
        }
        else if(now_sum == max_sum && now_len > max_len){
            max_sum = now_sum;
            max_len = now_len;
            max_first = now_first;
        }
        else if(now_sum == max_sum && now_len == max_len && now_first > max_first){
            max_sum = now_sum;
            max_len = now_len;
            max_first = now_first;
        }
        // printf("%d %d %d\n", now_sum, now_len, now_first);
        // printf("%d %d %d\n", max_sum, max_len, max_first);
 
    }
    printf("%d %d %d\n", max_sum, max_len, max_first);
}