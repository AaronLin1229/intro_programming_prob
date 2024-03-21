#include "testlib.h"

static inline bool check_eq(double a, double b){
    return abs(a - b) <= (double)1e-6;
}

int main(int argc, char * argv[]) {
    registerTestlibCmd(argc, argv);

    int a = inf.readInt(), b = inf.readInt(), c = inf.readInt();
    int n = ouf.readInt();
    double x1, x2;

    int delta = b * b - 4 * a * c;
    if(delta > 0){
        if(n != 2) quitf(_wa, "expected 2 solutions");

        x1 = ouf.readDouble();
        x2 = ouf.readDouble();
        double real_sol_x1 = ((double)-b - (double)sqrt(delta)) / ((double)2 * (double)a);
        double real_sol_x2 = ((double)-b + (double)sqrt(delta)) / ((double)2 * (double)a);

        if(!check_eq(real_sol_x1, x1)) quitf(_wa, "expected %lf, get %lf", real_sol_x1, x1);
        if(!check_eq(real_sol_x2, x2)) quitf(_wa, "expected %lf, get %lf", real_sol_x2, x2);
        quitf(_ok, "correct");
    }
    else if(delta == 0){
        if(n != 1) quitf(_wa, "expected 1 solution");
        
        x1 = ouf.readDouble();
        double real_sol_x1 = ((double)-b) / ((double)2 * (double)a);

        if(!check_eq(real_sol_x1, x1)) quitf(_wa, "expected %lf, get %lf", real_sol_x1, x1);
        quitf(_ok, "correct");
    }
    else{ // delta < 0
        if(n != 0) quitf(_wa, "expected 0 solution");
        
        quitf(_ok, "correct");
    }
}