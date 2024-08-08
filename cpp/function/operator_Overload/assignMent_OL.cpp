// you can overload constructor as such :
#include <iostream>
using namespace std;

class complex {
   private:
    int a, b;

   public:
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
    void operator=(complex x) {
        // i am comment
        cout << "Calling showData inside OpOL\n";
        x.showData();
        a = 55;
        b = 65;
    }
    void showData() {
        // display the value of a and b
        cout << "a = " << a << " b = " << b << endl;
    }
};

int main(void) {
    complex c1, c2(3);
    // c2 = c1;
    // c2 = (c1);
    c1.operator=(c2);
    cout << "..............\n";
    c1.showData();
    c2.showData();
    cout << "..............\n";
    return 0;
}