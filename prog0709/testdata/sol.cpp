#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<string> strings(N);
    for (int i = 0; i < N; ++i) {
        cin >> strings[i];
    }

    sort(strings.begin(), strings.end());

    for (const string& str : strings) {
        cout << str << endl;
    }

    return 0;
}
