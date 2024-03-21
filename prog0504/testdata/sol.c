#include <stdio.h>

int numlis[100000] = {0};
int alis[200005] = {0};
 
int main(void) {
  int n;
  int m;
  int temp;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    scanf("%d", &numlis[i]);
  }
  scanf("%d", &m);
  for(int i = 0; i < n; i++){
    alis[ numlis[i] % m ]++;
  }
  for(int i = 0; i < m; i++){
    printf("%d\n", alis[i]);
  }
}