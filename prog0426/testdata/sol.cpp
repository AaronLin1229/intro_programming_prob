#include <iostream>
using namespace std;
 
static inline int r(int x1, int y1, int x2, int y2){
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
}
 
int main(){
    int xa, ya, ra, xb, yb, rb;
    cin >> xa >> ya >> ra >> xb >> yb >> rb;
    ra *= ra, rb *= rb;
 
    int x, y;
    while(cin >> x >> y){
        int r1 = r(xa, ya, x, y);
        int r2 = r(xb, yb, x, y);
 
        if(r1 > ra && r2 > rb) cout << "Out" << endl;
        else if(r1 < ra || r2 < rb) cout << "In" << endl;
        else cout << "On" << endl;
    }
}