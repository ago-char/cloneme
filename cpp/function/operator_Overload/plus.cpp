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
        cout << "The Number = " << a << "i+" << b << "j" << endl;
        cout << ".......................\n";
    }
    // plus operator will have 2 operand, one operand is calling obj and
    // another is in formal argc and will return once addition is done
    complex operator+(complex x) {
        complex temp;
        temp.a = a + x.a;
        temp.b = b + x.b;
        return temp;
    }
};

int main(void) {
    // i am comment
    complex c1, c2(1), c3(9, 8), c4, c5;
    c2.showData();
    c3.showData();
    cout << "Adding c2 and c3 to assign result in c4\n";
    // call either this way (c2 called operator+ passing c3 as argc and returned
    // value is assigned to c4)
    c4 = c2.operator+(c3);
    cout << "Adding c1 and c2 to assign result in c5\n";
    // or this way (c1 called operator+ passing c2 as an argc and returned
    // value is assigned to c5)
    c5 = c1 + c2;
    c4.showData();
    c5.showData();
    return 0;
}