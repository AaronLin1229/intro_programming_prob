#include <bits/stdc++.h>
using namespace std;

int main(){
    int now_max_num = -1, cnt = 0;
    int x;
    while(scanf("%d", &x) != EOF){
        if(x > now_max_num){
            now_max_num = x;
            cnt = 1;
        }
        else if(x == now_max_num){
            cnt++;
        }

        printf("%d %d\n", now_max_num, cnt);
    }
}