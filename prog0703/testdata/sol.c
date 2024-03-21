#include <stdio.h>
#include <string.h>
 
static inline int max(int a, int b){
    return a > b ? a : b;
}
 
int main(){
    char ans[128] = {0}, ans_len = 0;
    char s[128] = {0}, s_len = 0;
 
    while(scanf("%s", s) != EOF){
        ans_len = strlen(ans);
        s_len = strlen(s);
 
        int start_idx = max(ans_len - s_len, 0);
        int overlap_cnt = ans_len - start_idx;
 
        for(int i = overlap_cnt; i >= 0; i--){
            if(strncmp(ans + start_idx + (overlap_cnt - i), s, i) == 0){
                strncpy(ans + start_idx + (overlap_cnt - i), s, s_len);    
                break;
            }
        }
    }
 
    printf("%s\n", ans);
}