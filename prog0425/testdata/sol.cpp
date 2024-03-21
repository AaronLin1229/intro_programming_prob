#include <bits/stdc++.h>
using namespace std;
 
int myabs(int n){
    if(n < 0) return -n;
    return n;
}
 
int main(){
    int n1, n2;
    cin >> n1 >> n2;
    int s1[4], s2[4];
    for(int i = 3; i >= 0; i--){
        s1[i] = n1 % 10;
        s2[i] = n2 % 10;
        n1 /= 10;
        n2 /= 10;
    }
    int a = 0, b = 0;
    for(int i = 0; i < 4; i++){
        if(s1[i] == s2[i]) a++;
    }
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(i == j) continue;
            if(s1[i] == s2[j]){
                b++;
                break;
            }
        }
    }

    cout << a << "A" << b << "B" << endl;
}