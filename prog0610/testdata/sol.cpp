#include <bits/stdc++.h>
using namespace std;

#define MAXN 128

static int delta[2][9] = {
    {0, 0, 0, 1, 0, 0, 0, 0, 0},
    {0, 0, 1, 1, 0, 0, 0, 0, 0}
};

static inline bool is_valid(int x, int y, int n){
    return x >= 0 && x < n && y >= 0 && y < n;
}

static inline int count(int x, int y, int board[MAXN][MAXN], int n){
    static int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

    int cnt = 0;
    for(int d = 0; d < 8; d++){
        int this_x = x + dx[d], this_y = y + dy[d];
        if(is_valid(this_x, this_y, n)) cnt += board[this_x][this_y];
    }
    return cnt;
}

void step(int board[MAXN][MAXN], int n){
    int temp[MAXN][MAXN];
    for(int i = 0; i < n; i++){ 
        for(int j = 0; j < n; j++){
            temp[i][j] = delta[board[i][j]][count(i, j, board, n)];
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            board[i][j] = temp[i][j];
        }
    }
}

void print_board(int board[MAXN][MAXN], int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << board[i][j] << (j == n - 1 ? '\n' : ' ');
        }
    }
}

int main() {
    int n, board[MAXN][MAXN];
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> board[i][j];
        }
    }

    int m;
    scanf("%d", &m);
    while(m--){ 
        step(board, n);
    }
    print_board(board, n);
}
