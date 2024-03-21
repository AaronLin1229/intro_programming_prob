#include <stdio.h>
#include <stdlib.h>
#define bool int
#define true 1
#define false 0
 
 
int min(int a, int b){
    if(a < b) return a;
    return b;
}
 
int max(int a, int b){
    if(a > b) return a;
     return b;
}
 
int main(){
    int x, y;
    int minX = 20000, maxX = -20000;
    int minY = 20000, maxY = -20000;
    while(scanf("%d %d", &x, &y) != EOF){
        minX = min(minX, x);
        maxX = max(maxX, x);
        minY = min(minY, y);
        maxY = max(maxY, y);
    }
    printf("%d", (maxX - minX) * (maxY - minY));
}