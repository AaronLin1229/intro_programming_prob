#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int r, c;
int arr[512][512] = {0};
const int dx[4] = {0, 0, 1, -1};
const int dy[4] = {1, -1, 0, 0};
 
static inline int is_valid(int x, int y){
    return x >= 0 && y >= 0 && x < r && y < c;
}
 
void check(int x, int y, int d1, int d2){
    int x1 = x + dx[d1], y1 = y + dy[d1];
    int x2 = x + dx[d2], y2 = y + dy[d2];
    if(!is_valid(x1, y1) || !is_valid(x2, y2)) return;
 
    if(arr[x][y] == arr[x1][y1] && arr[x][y] == arr[x2][y2]){
        arr[x][y] = 0;
        arr[x1][y1] = 0;
        arr[x2][y2] = 0;
    }
}
 
int main(){
    scanf("%d %d", &r, &c);
    for(int i = 0; i < r; i++) for(int j = 0; j < c; j++) scanf("%d", &arr[i][j]);
 
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            for(int d1 = 0; d1 < 4; d1++){
                for(int d2 = d1 + 1; d2 < 4; d2++){
                    check(i, j, d1, d2);
                }
            }
        }
    }
 
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            printf("%d%c", arr[i][j], (j == c - 1) ? '\n' : ' ');
        }
    }
}