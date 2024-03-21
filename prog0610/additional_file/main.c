#include <stdio.h>
#define MAXN 128

void step(int board[MAXN][MAXN], int n){
    // your code here
}

void print_board(int board[MAXN][MAXN], int n){
    // your code here
}

int main() {
    int n, board[MAXN][MAXN];
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf("%d", &board[i][j]);
        }
    }

    int m;
    scanf("%d", &m);
    while(m--){ 
        step(board, n);
    }
    print_board(board, n);
}
