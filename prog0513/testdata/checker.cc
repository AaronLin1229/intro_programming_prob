#include <utility>
#include "testlib.h"
using namespace std;

pair<double, double> solve(){
    int n = inf.readInt();
    vector<double> v(n);
    for(int i = 0; i < n; i++) v[i] = inf.readDouble();

    double sum = 0;
    for(double &x: v){
        sum += x;
    }
    double mean = sum / v.size();

    double sq_diff_sum = 0.0;
    for(double &x: v){
        sq_diff_sum += (x - mean) * (x - mean);
    }
    double var = sq_diff_sum / v.size();

    return {mean, var};
}
bool eq(double x, double y){
    return abs(x - y) <= (double)1e-6;
}

int main(int argc, char * argv[]) {
    registerTestlibCmd(argc, argv);

    pair<double, double> p = solve();
    double correct_avg = p.first;
    double correct_var = p.second;
    
    double usr_avg = ouf.readDouble();
    double usr_var = ouf.readDouble();
    
    if(eq(correct_avg, usr_avg) && eq(correct_var, usr_var)){
        quitf(_ok, "avg = %lf, var = %lf", usr_avg, usr_var);
    }

    if(!eq(correct_avg, usr_avg)){
        quitf(_wa, "avg: expected  %lf, got %lf", correct_avg, usr_avg);
    }
    if(!eq(correct_var, usr_var)){
        quitf(_wa, "var: expected  %lf, got %lf", correct_var, usr_var);
    }

    quitf(_wa, "error");
}