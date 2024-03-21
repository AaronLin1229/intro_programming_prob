#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    if(A == B) cout << "no bigger!";
    else cout << max(A, B);
    return 0;
}
