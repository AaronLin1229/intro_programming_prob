#include "testlib.h"

int main(int argc, char * argv[]) {
    registerTestlibCmd(argc, argv);
    
    double in_f = inf.readDouble();
    double real_c = (in_f - 32) * 5 / 9;
    double out_c = ouf.readDouble();
    
    if(abs(real_c - out_c) <= (double)1e-6){
        quitf(_ok, "answer is near %lf", real_c);
    }
    else{
        quitf(_wa, "output is %lf answer is %lf", out_c, real_c);
    }
}