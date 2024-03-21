#include <bits/stdc++.h>
using namespace std;
 
struct pt{
    int x;
    int y;
};
 
int main(){
    pt a, b, c, d;
    cin  >> a.x >> a.y >> b.x >> b.y >> c.x >> c.y >> d.x >> d.y;
 
    int area = 0;
    area += (b.x - a.x) * (b.y - a.y);
    area += (c.x - a.x) * (d.y - b.y);
    area += (c.x - d.x) * (c.y - d.y);
 
    int per = 0;
    per += 2 * (c.x - a.x + c.y - a.y);
    
    cout << per << endl;
    cout << area << endl;
}