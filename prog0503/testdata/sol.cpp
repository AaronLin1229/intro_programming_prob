#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n,sum,avg,total,num=0;
    while(cin>>n&&n)
    {
        num++;
        int a[n];
        sum=0;
        total=0;
        for(int i=0;i<n;i++)
        {
            cin >> a[i];
            sum += a[i];
        }
        avg = sum/n;
        cout<<"Set #"<<num<<endl;
        for(int i=0;i<n;i++)
            total+=abs(a[i]-avg);
        cout<<"The minimum number of moves is "<<total/2<<"."<<endl;
    }
}