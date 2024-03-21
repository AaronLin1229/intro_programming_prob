#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
static inline int sign(int k){
    if(k > 0) return 1;
    else return -1;
}
 
int main(){
    int last, now; scanf("%d", &last);
    int cnt = 1;
    while(scanf("%d", &now) == 1){
        if(sign(now) == sign(last)) cnt++;
        else{
            printf("%d ", cnt * sign(last));
            cnt = 1;
        }
        last = now;
    }
    printf("%d\n", cnt * sign(last));
}