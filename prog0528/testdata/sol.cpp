#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[128][128] = {0};
int temp[128][128] = {0};

bool is_valid(int x, int y){
    return x >= 0 && y >= 0 && x < n && y < m;
}

int count_neighbor(int x, int y){
    static int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

    int cnt = 0;
    for(int d = 0; d < 8; d++){
        int this_x = x + dx[d], this_y = y + dy[d];
        if(is_valid(this_x, this_y)) cnt += arr[this_x][this_y];
    }
    return cnt;
}

void update(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            int cnt = count_neighbor(i, j);

            if(arr[i][j] == 1){
                if(cnt == 2 || cnt == 3) temp[i][j] = 1;
                else temp[i][j] = 0;
            }
            if(arr[i][j] == 0){
                if(cnt == 3) temp[i][j] = 1;
                else temp[i][j] = 0;
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            arr[i][j] = temp[i][j];
        }
    }
}

int main(){
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    
    int k; scanf("%d", &k);
    while(k--){
        update();
    }
        

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            printf("%d%c", arr[i][j], (j == m - 1) ? '\n' : ' ');
        }
    }
}