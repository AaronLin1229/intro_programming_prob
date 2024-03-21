#include <stdio.h>
 
void printarr(int arr[], int n){
  if(n == 0) return;
  for(int i = 0; i < n - 1; i++){
    printf("%d ", arr[i]);
  }
  printf("%d", arr[n - 1]);
  return;
}
 
int main(void) {
  int even[1005] = {0};
  int odd[1005] = {0};
  int temp;
  int n;
  int cnteven = 0;
  int cntodd = 0;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    scanf("%d", &temp);
    if(temp % 2 == 0){
      even[cnteven] = temp;
      cnteven++;
    }
    else{
      odd[cntodd] = temp;
      cntodd++;
    }
  }
  printarr(odd, cntodd);
  printf("\n");
  printarr(even, cnteven);
 
}