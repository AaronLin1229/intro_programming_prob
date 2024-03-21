#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    string rev_s = s;
    reverse(rev_s.begin(), rev_s.end());
    cout << (s == rev_s ? "YES" : "NO") << endl;
    return 0;
}
