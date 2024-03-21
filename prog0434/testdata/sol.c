#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(){
    int n; scanf("%d", &n); n--;
 
    int last_x, last_y, last_w, last_h; scanf("%d %d %d %d", &last_x, &last_y, &last_w, &last_h);
    int ans = last_w * last_h;
 
    last_x += last_w, last_y += last_h;
    for(int i = 0; i < n; i++){
        int this_x, this_y, this_w, this_h; scanf("%d %d %d %d", &this_x, &this_y, &this_w, &this_h);
        ans += this_w * this_h;
        ans -= (last_x - this_x) * (last_y - this_y);
        last_x = this_x + this_w, last_y = this_y + this_h;
    }
    printf("%d\n", ans);
}