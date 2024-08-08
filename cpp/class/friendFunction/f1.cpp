// obviously f stands for friend
#include <iostream>
using namespace std;
class complex {
    int a, b;

   public:
    complex(int x = 0, int y = 0) {
        a = x;
        b = y;
    }
    void display() { cout << a << " and " << b << endl; }
    // 1. friend function should be declared inside class(if definition is
    // outside class), does not matter you declare it private, public or
    // protected coz it does not require calling obj as it is not memnber func
    friend complex add(complex N1, complex N2);
};

// 2. friend function should be defined outside, remember no use of friend
// keyword
complex add(complex N1, complex N2) {
    complex t;
    // 3. friend function can access public, protected or even private members
    t.a = N1.a + N2.a;
    t.b = N1.b + N2.b;
    return t;
}

int main(void) {
    // i am comment
    complex n1(2), n2(9, 7);
    complex n3 = add(n1, n2);
    n3.display();
    return 0;
}