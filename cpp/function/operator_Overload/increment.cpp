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
        // cout << "\nDefinite Part = " << a << endl;
        // cout << "Imagenary Part = " << b << endl;
        if (b >= 0)
            cout << "The Number = " << a << "i+" << b << "j" << endl;
        else
            cout << "The Number = " << a << "i-" << -b << "j" << endl;
        cout << ".......................\n";
    }
    // unary pre increment operator will have just 1 operaotr which is calling
    // obj, remember no argc in parameterList
    complex operator++() {
        complex t;
        t.a = ++a;
        t.b = ++b;
        return t;
    }
    // unary post increment operator will only have one argc which is calling
    // obj, just to differentiate it from pre increment one dummy formal argc is
    // listed i.e (int)
    complex operator++(int) {
        complex t;
        t.a = a++;
        t.b = b++;
        return t;
    }
};

// Driver Code
int main(void) {
    complex c1, c2(8), c3(0, 9), c4(7, 4);
    cout << "c1 and c4 at start :" << endl;
    c1.showData();
    c4.showData();
    cout << "c4 is pre incremented and result at c1, now c1 and c4 :" << endl;
    c1 = ++c4;
    c1.showData();
    c4.showData();
    cout << "c4 is post incremented and result at c1, now c1 and c4" << endl;
    c1 = c4++;
    c1.showData();
    c4.showData();
    return 0;
}