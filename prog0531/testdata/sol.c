#include <stdio.h>
#include <stdlib.h>
 
int n, m;
int w[16][16] = {0};
int t;
 
int p[16][16] = {0};
 
void train(){
    int label; scanf("%d", &label);
    for(int i = 0; i < m; i++) for(int j = 0; j < m; j++) scanf("%d", &p[i][j]);
 
    int ans = 0;
    for(int i = 0; i < m; i++) for(int j = 0; j < m; j++) ans += (p[i][j] * w[i][j]);
    int cfy = (ans >= t);
 
    // printf("label = %d, cfy = %d\n", label, cfy);
 
    if(label == 1 && !cfy){
        for(int i = 0; i < m; i++) for(int j = 0; j < m; j++){
            if(p[i][j]) w[i][j] *= 2;
        }
    }
    else if(label == 0 && cfy){
        for(int i = 0; i < m; i++) for(int j = 0; j < m; j++){
            if(p[i][j]){
                w[i][j] /= 2;
                if(w[i][j] == 0) w[i][j] = 1;
            }
        }
    }
}
void test(){
    for(int i = 0; i < m; i++) for(int j = 0; j < m; j++) scanf("%d", &p[i][j]);
 
    int ans = 0;
    for(int i = 0; i < m; i++) for(int j = 0; j < m; j++) ans += (p[i][j] * w[i][j]);
    int cfy = (ans >= t);
    printf("%d\n", cfy);
}
 
int main(){
    scanf("%d %d", &n, &m);
    for(int i = 0; i < m; i++) for(int j = 0; j < m; j++) w[i][j] = 1;
    t = 2 * m * m;
 
    while(n--){
        train();
        /*
        for(int i = 0; i < m; i++){
            for(int j = 0; j < m; j++){
                printf("%d ", w[i][j]);
            }
            printf("\n");
        }
        printf("================\n");
        */
    }
 
    int q; scanf("%d\n", &q);
    while(q--){
        test();
    }
}