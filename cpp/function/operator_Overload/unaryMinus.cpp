#include <iostream>
using namespace std;

class complex {
   private:
    int a, b;

   public:
    complex(int x = 0, int y = 0) {
        a = x;
        b = y;
    }
    void showData(void) {
        cout << "\nDefinite Part = " << a << endl;
        cout << "Imagenary Part = " << b << endl;
        if (b > 0)
            cout << "The Number = " << a << "i+" << b << "j" << endl;
        else
            cout << "The Number = " << a << "i-" << -b << "j" << endl;
        cout << ".......................\n";
    }
    // unary minus operator will have 1 operand, which is of course calling obj
    complex operator-() {
        complex temp;
        temp.a = -a;
        temp.b = -b;
        return temp;
    }
};

// Driver Code
int main(void) {
    complex c1, c2(8), c3(0, 9), c4(7, 4);
    c4.showData();
    complex c5 = -c4;
    c5.showData();
    return 0;
}