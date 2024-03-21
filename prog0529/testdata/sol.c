#include <stdio.h>
#include <assert.h>

#define MAXLEN 1000
static int snake[MAXLEN*MAXLEN];
static int result[MAXLEN*MAXLEN];

void SpiralSnake(int n, int *snake, int *result){
    int arr[999][999];
 
    int now_x = n / 2, now_y = n / 2;
 
    int t = 0;
    arr[now_x][now_y] = snake[t++];
    for(int i = 0; i < n / 2; i++){
        now_y--, arr[now_x][now_y] = snake[t++];
 
        for(int j = 0; j < 2 * i + 1; j++) now_x--, arr[now_x][now_y] = snake[t++];
        for(int j = 0; j < 2 * i + 2; j++) now_y++, arr[now_x][now_y] = snake[t++];
        for(int j = 0; j < 2 * i + 2; j++) now_x++, arr[now_x][now_y] = snake[t++];
        for(int j = 0; j < 2 * i + 2; j++) now_y--, arr[now_x][now_y] = snake[t++];
    }
 
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            result[i * n + j] = arr[i][j];
        }
    }
}

 
int main(){
    int N;
    while(scanf("%d", &N)!=EOF){
        for(int i=0; i<N*N; i++)
              assert(scanf("%d", &snake[i])==1);
        SpiralSnake(N, snake, result);
        for(int i=0; i<N*N; i++)
             printf("%d%c", result[i], " \n"[i==N*N-1]);
    }
    return 0;
}