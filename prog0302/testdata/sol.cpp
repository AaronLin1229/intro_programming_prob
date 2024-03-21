#include <bits/stdc++.h>
using namespace std;

int main() {
    char ch;
    cin >> ch;
    if (isupper(ch) && string("AEIOU").find(ch) != string::npos) {
        cout << ch << " is class A\n";
    } else if (islower(ch) && string("aeiou").find(ch) != string::npos) {
        cout << ch << " is class B\n";
    } else if (isupper(ch)) {
        cout << ch << " is class C\n";
    } else {
        cout << ch << " is class D\n";
    }
    return 0;
}
