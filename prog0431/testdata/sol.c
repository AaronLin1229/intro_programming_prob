#include <stdio.h>
 
static inline int sign(int x){
    if(x > 0) return 1;
    else return -1;
}
 
int main(){
    int last_num, now_num;
    if(scanf("%d %d", &last_num, &now_num) != 2){
        printf("0\n");
        return 0;
    }
 
    int i = 3;
    int last_sign = sign(now_num - last_num), now_sign;
    int max_len = 0, max_left = 0, max_idx = 0;
    last_num = now_num;
 
    int last_cnt = 0, now_cnt = 1;
    while(scanf("%d", &now_num) != EOF){
        now_sign = sign(now_num - last_num);
        if(last_sign == now_sign) now_cnt++;
        else {last_cnt = now_cnt; now_cnt = 1;}
 
        int this_cnt = last_cnt + now_cnt + 1;
        if(last_cnt != 0){
            if(this_cnt > max_len || (this_cnt == max_len && last_cnt > max_left)){
                max_len = this_cnt;
                max_left = last_cnt;
                max_idx = i - this_cnt + 1;
            }
        }
 
        // printf("i = %d, nums: (%d, %d), signs: (%d %d)\n", i, last_num, now_num, last_sign, now_sign);
        // printf("last cnt: %d, now cnt: %d\n", last_cnt, now_cnt);
        // printf("max infos: %d %d %d\n", max_len, max_left, max_idx);
 
        last_sign = now_sign;
        last_num = now_num;
        i++;
    }
    if(max_len != 0) printf("%d %d\n", max_len, max_idx);
    else printf("0\n");
}