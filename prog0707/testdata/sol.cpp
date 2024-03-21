#include <bits/stdc++.h>
using namespace std;

string formatWithCommas(string number) {
    string result;
    int length = number.length();
    int count = 0;

    for (int i = length - 1; i >= 0; i--) {
        result = number[i] + result;
        if (++count % 3 == 0 && i != 0) {
            result = "," + result;
        }
    }
    return result;
}

int main() {
    string n;
    cin >> n;
    cout << formatWithCommas(n) << endl;
    return 0;
}
