#include <bits/stdc++.h>
using namespace std;

int main() {
    int quantities[5];
    int prices[5] = {40, 30, 20, 50, 50};
    int total = 0;
    for (int i = 0; i < 5; ++i) {
        cin >> quantities[i];
        total += quantities[i] * prices[i];
    }
    cout << total << endl;
    return 0;
}
