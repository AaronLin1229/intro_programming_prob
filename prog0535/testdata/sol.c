#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int h, w, k;
int arr[200][200] = {0};
 
int find_sum(int x, int y){
    int cnt = 0;
    for(int i = - (k - 1); i <= k - 1; i++){
        if(i == -(k - 1) || i == (k - 1)) cnt += arr[x + i][y];
        else{
            int dy = k - abs(i) - 1;
            cnt += arr[x + i][y + dy];
            cnt += arr[x + i][y - dy];
        }
    }
    return cnt;
}
 
int main(){
    scanf("%d %d %d", &h, &w, &k);
    for(int i = 0; i < h; i++) for(int j = 0; j < w; j++) scanf("%d", &arr[i][j]);
 
    int max_num = 0;
    for(int i = (k - 1); i <= (h - k); i++){
        for(int j = (k - 1); j <= (w - k); j++){
            int s = find_sum(i, j);
            if(s > max_num) max_num = s;
        }
    }
 
    printf("%d\n", max_num);
}