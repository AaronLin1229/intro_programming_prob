#include <bits/stdc++.h>
using namespace std;

int main() {
    int p;
    cin >> p;
    int currencies[] = {1000, 500, 100, 50, 10, 5, 1};
    int count = 0;
    for (int i = 0; i < 7; ++i) {
        count += p / currencies[i];
        p %= currencies[i];
    }
    cout << count << endl;
    return 0;
}
