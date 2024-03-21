#include <bits/stdc++.h>
using namespace std;

int main() {
    char ch;
    int sum_a = 0, sum_b = 0;
    bool flag = false;

    while (cin >> ch){
        if(!(ch >= '0' && ch <= '9')) break;

        if(flag){
            sum_a += ch - '0';
        }
        else{
            sum_b += ch - '0';
        }

        flag = !flag;
    }

    int diff = sum_a - sum_b;
    if(diff < 0) diff = -diff;

    if(diff % 11 == 0) cout << "YES" << endl;
    else cout << "NO" << endl; 
}
