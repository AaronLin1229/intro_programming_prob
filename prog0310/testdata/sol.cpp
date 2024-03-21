#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int w, a, b, c, d, e, ans;
    cin >> w >> a >> b >> c >> d >> e;
    if(b != 0){
        ans = w * w + (a + b + c + 2 * d + 2 * e + 2) * (a + b + c+ 2 * d + 2 * e + 2);
    }
    else{
        int m = (d > e) ? d : e;
        ans = w * w + (a + c + 2 * m + 2) * (a + c + 2 * m + 2);
    }
    cout << ans << endl;
}