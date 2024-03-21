#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    cout << (a + b) * (b - a + 1) / 2 << endl;
    cout << a + b + 2 * (b - a - 1) << endl;
}