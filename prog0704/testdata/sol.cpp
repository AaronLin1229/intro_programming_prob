#include <bits/stdc++.h>
using namespace std;

string remove_leading_zeros(string s){
    int idx = 0;
    for(idx = 0; idx < s.size(); idx++){
        if(s[idx] != '0') break;
    }

    string rtv = s.substr(idx);
    if(rtv == "") rtv = "0";

    return rtv;
}

int main() {
    string s;
    cin >> s;
    cout << remove_leading_zeros(s) << endl;
}