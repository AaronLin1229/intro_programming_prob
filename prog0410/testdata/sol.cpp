#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int x1, y1; cin >> x1 >> y1;
 
    int this_x, this_y, last_x = x1, last_y = y1;
    int ans = 0;
    for(int i = 0; i < n; i++){
        cin >> this_x >> this_y;
        ans += last_x * this_y - last_y * this_x;
        last_x = this_x, last_y = this_y;
    }
    ans += last_x * y1 - last_y * x1;
    cout << ans << endl;
}