#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
 
int n, m, l, w;
int x = 0, y = 0;
int now_x, now_y;
int map[512][512] = {0};
 
const int dx[6] = {0, 0, 1, 0, -1, 1};
const int dy[6] = {0, 1, 0, -1, 0, 1};
 
void print_map(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            printf("%d", map[i][j]);
        }
        printf("\n");
    }
}
 
void move_1(){
    if(y + w >= m) return;
 
    int cnt = 0;
    for(int i = 0; i < l; i++){
        now_x = x + i, now_y = y + w;
        if(map[now_x][now_y] == 2) cnt++;  
    }
    if(cnt >= 2) return;
    else{
        for(int i = 0; i < l; i++){
            now_x = x + i, now_y = y;
            map[now_x][now_y] = 0;  
        }
        for(int i = 0; i < l; i++){
            now_x = x + i, now_y = y + w;
            map[now_x][now_y] = 1;
        }
        y++;
    }
}
void move_2(){
    if(x + l >= n) return;
 
    int cnt = 0;
    for(int i = 0; i < w; i++){
        now_x = x + l, now_y = y + i;
        if(map[now_x][now_y] == 2) cnt++;  
    }
    if(cnt >= 2) return;
    else{
        for(int i = 0; i < w; i++){
             now_x = x, now_y = y + i;
            map[now_x][now_y] = 0;  
        }
        for(int i = 0; i < w; i++){
            now_x = x + l, now_y = y + i;
            map[now_x][now_y] = 1;
        }
        x++;
    }
}
void move_3(){
    if(y - 1 < 0) return;
 
    int cnt = 0;
    for(int i = 0; i < l; i++){
        now_x = x + i, now_y = y - 1;
        if(map[now_x][now_y] == 2) cnt++;  
    }
    if(cnt >= 2) return;
    else{
        for(int i = 0; i < l; i++){
            now_x = x + i, now_y = y + w - 1;
            map[now_x][now_y] = 0;  
        }
        for(int i = 0; i < l; i++){
            now_x = x + i, now_y = y - 1;
            map[now_x][now_y] = 1;
        }
        y--;
    }
}
void move_4(){
    if(x - 1 < 0) return;
 
    int cnt = 0;
    for(int i = 0; i < w; i++){
        now_x = x - 1, now_y = y + i;
        if(map[now_x][now_y] == 2) cnt++;  
    }
    if(cnt >= 2) return;
    else{
        for(int i = 0; i < w; i++){
            now_x = x + l - 1, now_y = y + i;
            map[now_x][now_y] = 0;  
        }
        for(int i = 0; i < w; i++){
            now_x = x - 1, now_y = y + i;
            map[now_x][now_y] = 1;
        }
        x--;
    }
}
 
void move_5(){
    if(y + w >= m || x + l >= n) return;
 
    int cnt = 0;
    for(int i = 1; i < l; i++){
        now_x = x + i, now_y = y + w;
        if(map[now_x][now_y] == 2) cnt++;  
    }
    for(int i = 1; i < w; i++){
        now_x = x + l, now_y = y + i;
        if(map[now_x][now_y] == 2) cnt++;  
    }
    if(map[x + l][y + w] == 2) cnt++;
 
    if(cnt >= 2) return;
    else{
        for(int i = 0; i < l; i++){
            now_x = x + i, now_y = y;
            map[now_x][now_y] = 0;  
        }
        for(int i = 0; i < w; i++){
            now_x = x, now_y = y + i;
            map[now_x][now_y] = 0;  
        }
 
        for(int i = 1; i < l; i++){
            now_x = x + i, now_y = y + w;
            map[now_x][now_y] = 1;
        }
        for(int i = 1; i < w; i++){
            now_x = x + l, now_y = y + i;
            map[now_x][now_y] = 1;
        }
        map[x + l][y + w] = 1;
 
        x++, y++;
    }
}
 
 
int main(){
    // ipt
    scanf("%d %d %d %d", &n, &m, &l, &w);
    int o; scanf("%d", &o);
    while(o--){
        int a, b; scanf("%d %d", &a, &b);
        map[b][a] = 2;
    } 
    for(int i = 0; i < l; i++){
        for(int j = 0; j < w; j++){
            map[i][j] = 1;
        }
    }
 
    int q;
    while(scanf("%d", &q) != EOF){
        if(q == 0) print_map();
        else if(q == 1) move_1();
        else if(q == 2) move_2();
        else if(q == 3) move_3();
        else if(q == 4) move_4();
        else if(q == 5) move_5();
 
        /*
        printf("%d\n", q);
        print_map();
        printf("\n");
        */
    }
}