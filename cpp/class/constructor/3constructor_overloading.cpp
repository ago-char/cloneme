// you can overload constructor as such :
#include <iostream>
using namespace std;

class complex {
   private:
    int a, b;
    // version1 no argc req
    complex() {
        a = 0;
        b = 0;
    }
    // version2 1 argc req
    complex(int x) {
        a = x;
        b = 0;
    }
    // version3 2 argc req
    complex(int x, int y) {
        a = x;
        b = y;
    }
};

int main(void) { return 0; }