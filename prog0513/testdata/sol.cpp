#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    double arr[n] = {0};
    for(int i = 0; i < n; i++) cin >> arr[i];
 
    double avg = 0;
    for(int i = 0; i < n; i++) avg += arr[i];
    avg /= (double)n;
 
    double var = 0;
    for(int i = 0; i < n; i++) var += ((arr[i] - avg) * (arr[i] - avg));
    var /= (double)n;
 
    cout << setprecision(15) << avg << endl;
    cout << setprecision(15) << var << endl;
}