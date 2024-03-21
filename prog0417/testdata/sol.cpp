#include <bits/stdc++.h>
using namespace std;

int main() {
    int k;
    string line;
    cin >> k; cin.ignore();
    k = (k + 26000) % 26;
    
    char ch;
    while((ch = getchar()) != EOF){
        char ans;
        if(!isalpha(ch)) ans = ch;
        else if(isupper(ch)){
            ans = (((ch - 'A') + k) % 26) + 'A';
        }
        else if(islower(ch)){
            ans = (((ch - 'a') + k) % 26) + 'a';
        }
        cout << ans;
    }
    cout << endl;
}
